          
from graphe import graphe 
from pyamaze import maze,agent,COLOR

g=graphe(3,3)
g.ajoutNoeud(0,0)
g.ajoutArc(0,0,0,1,1)
g.ajoutArc(0,0,1,0,1)

g.ajoutNoeud(0, 1)
g.ajoutArc(0,1,0,0,1)
g.ajoutArc(0,1,0,2,1)
g.ajoutArc(0,1,1,1,1)

g.ajoutNoeud(0, 2)
g.ajoutArc(0,2,0,1,1)
g.ajoutArc(0,2,1,2,1)

g.ajoutNoeud(1,0)
g.ajoutArc(1,0,0,0,1)
g.ajoutArc(1,0,2,0,1)
g.ajoutArc(1,0,1,1,1)

g.ajoutNoeud(1,1)
g.ajoutArc(1,1,1,0,1)
g.ajoutArc(1,1,0,1,0)
g.ajoutArc(1,1,1,2,0)
g.ajoutArc(1,1,2,1,0)

g.ajoutNoeud(1,2)
g.ajoutArc(1,2,0,2,1)
g.ajoutArc(1,2,1,1,0)
g.ajoutArc(1,2,2,2,1)

g.ajoutNoeud(2,0)
g.ajoutArc(2,0,2,1,0)
g.ajoutArc(2,0,1,0,1)

g.ajoutNoeud(2,1)
g.ajoutArc(2,1,2,0,0)
g.ajoutArc(2,1,1,1,0)
g.ajoutArc(2,1,2,2,0)

g.ajoutNoeud(2,2)
g.ajoutArc(2,2,2,1,0)
g.ajoutArc(2,2,1,2,1)


# g.afficheGraphiMatri()
# g.listerArcs()
# g.listerNoeud()
g.adjasNoeud(0,1)
print (g.succ((1,0)))
print (g.succ((2,2)))
print (g.succ((0,1)))
print ("(0,0):",g.succ((0,0)))
print("DFS")
print(g.dfs((0,0),(2,2)))
print("BFS")
print(g.bfs((0,0),(2,2)))
print(("LDFS"))
print(g.ldfs((0, 0), (2, 2), 3))
print("IDDFS")
print(g.iddfs((0, 0), (2, 2)))


# # If a path is found, visualize it
# if found:
#     print("Path found:", path)
#     a = agent(m, footprints=True, filled=True, color=COLOR.red)
#     m.tracePath({a: [(i+1, j+1) for (i, j) in path]}, delay=300)
#     m.run()
# else:
#     print("No path found")