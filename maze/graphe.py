import networkx as nx
import matplotlib.pyplot as plt
from pile import piled  
from file import filed
from pyamaze import maze
class graphe:
    def __init__(self, L, C):
        self.l = L
        self.c = C
        self.g = {}
        self.m = maze(self.l, self.c)
        self.E=[]
        self.A=[]

    def ajoutNoeud(self, i, j):
        self.g[(i, j)] = []

    def ajoutArc(self, i, j, x, y,p): #tous les voisins  z prend 1 ou 0 
        self.g[(i, j)].append(((x, y),p))

    def affiche(self):
        print(self.g)

    def listerNoeud(self):
        for key, value in self.g.items():
            print(key)

    def listerArcs(self):
        for key, value in self.g.items():
            print(value)

    def adjasNoeud(self, i, j):
        for key, value in self.g.items():
            if (i, j) == key:
                print(value)

    def afficheGraphe(self):
        
        for noeud, arcs in self.g.items():
            print(noeud,arcs)

    def affichegraphiMatri(self):
        G = nx.self.g()
        for noeud, arcs in self.g.items():
            G.add_node(noeud)
            for arc in arcs:
                G.add_edge(noeud, arc[0], weight=arc[1])  # Ajoute un poids pour indiquer la présence d'un arc
                
        # Crée une disposition matricielle pour le self.ge
        pos = {(i, j): (j, -i) for i in range(self.l) for j in range(self.c)}
        
        # Dessine le self.ge avec les noms des nœuds et les poids des arêtes
        nx.draw_networkx(G, pos, with_labels=True)
        
        # Ajoute les poids des arêtes dans le dessin
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        plt.gca().invert_yaxis()  # Inverse l'axe y pour correspondre à une matrice
        plt.axis('equal')  # Égalise les proportions des axes x et y
        plt.show()
    
    def succ(self, x):
        (i, j) = x
        S=[]
        for key, value in self.g.items():
            if (i, j) == key:
                # print("value de",x,":",value)
                for tuple_value in value:
                    if (self.verif(tuple_value)==1) and (tuple_value[1] == 1):
                        S.append(tuple_value[0])
        return S 
    


    def verif(self ,x):
        (i,j)=x
        if i in self.E:
            return 0
        else :
            return 1
        
    def dfs(self, x, y):
        p = piled()
        self.A = []
        self.E=[]
        self.E.append(x)
        B={}
        p.empiler(x)
        while not p.pile_vide():
            curr = p.depiler()
            if curr == y:
                path = self._reconstruct_path(B, x, y)
                return True,B
            else:
                for i in self.succ(curr):
                    B[i] = curr 
                    p.empiler(i)  
                    self.E.append(i)
                      
        return False ,B # Return False if the stack becomes empty without finding 'y'
        
    
    def bfs(self, x, y):
        f = filed()
        self.A = []
        self.E=[]
        B={}
        self.E.append(x)
        f.enfiler(x)
        while not f.file_vide():
            curr = f.defiler()
            if curr == y:
                path = self._reconstruct_path(B, x, y)
                return True,B
            else:
                for i in self.succ(curr):
                    B[i] = curr
                    f.enfiler(i)  
                    self.E.append(i)        
        return False,B  
        
    def ldfs(self, x, y, depth, B=None):
        if B is None:
            B = {}
        if depth < 0:
            return False, B
        if x == y:
            path = self._reconstruct_path(B, x, y)
            return True, path
        if depth == 0:
            return False, B
        self.E.append(x)
        for i in self.succ(x):
            B[i] = x
            found, path = self.ldfs(i, y, depth - 1, B)
            if found:
                return True, path
        return False, B

    def iddfs(self, x, y):
        depth = 0
        while True:
            self.E = []  # Reset the list of explored nodes at each iteration
            found, path = self.ldfs(x, y, depth)
            if found:
                return found, path
            depth += 1


    def create_maze(self): 
        for (i, j), neighbors in self.g.items():
            for ((x, y), p) in neighbors:
                if p == 1:
                    if i == x:
                        if j < y:
                            self.m.maze_map[(i + 1, j + 1)]['E'] = 1
                            self.m.maze_map[(x + 1, y + 1)]['W'] = 1
                        else:
                            self.m.maze_map[(i + 1, j + 1)]['W'] = 1
                            self.m.maze_map[(x + 1, y + 1)]['E'] = 1
                    elif j == y:
                        if i < x:
                            self.m.maze_map[(i + 1, j + 1)]['S'] = 1
                            self.m.maze_map[(x + 1, y + 1)]['N'] = 1
                        else:
                            self.m.maze_map[(i + 1, j + 1)]['N'] = 1
                            self.m.maze_map[(x + 1, y + 1)]['S'] = 1
        return self.m
    

    def maze_to_graph(self):
        for i in range(self.m.rows):
            for j in range(self.m.cols):
                self.g[(i, j)] = []
                # Check East
                if j + 1 < self.m.cols and self.m.maze_map[(i + 1, j + 1)]['E']:
                    self.g[(i, j)].append(((i, j + 1), 1))
                # Check West
                if j - 1 >= 0 and self.m.maze_map[(i + 1, j + 1)]['W']:
                    self.g[(i, j)].append(((i, j - 1), 1))
                # Check North
                if i - 1 >= 0 and self.m.maze_map[(i + 1, j + 1)]['N']:
                    self.g[(i, j)].append(((i - 1, j), 1))
                # Check South
                if i + 1 < self.m.rows and self.m.maze_map[(i + 1, j + 1)]['S']:
                    self.g[(i, j)].append(((i + 1, j), 1))
        return self.g

    def _reconstruct_path(self, B, start, end):
        path = []
        current = end
        while current in B:
            path.append(current)
            current = B[current]
        path.append(start)
        path.reverse()
        return path


            
            
        
     
    
    
  