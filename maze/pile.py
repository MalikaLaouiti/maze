from collections import deque
class pile:
    def __init__(self) :
        self.l=[]

    def pile_vide(self):
        return len(self.l)==0
    
    def empiler(self,x):
        (self.l).append(x)
    
    def depiler(self):
        if not self.pile_vide():
            return self.l.pop()
        else:
            return None  

    def affichage(self):
        print(self.l)

    def taille_pile(self):
        print(len(self.l))

class piled:
    def __init__(self) :
        self.l=deque([])

    def pile_vide(self):
        return len(self.l)==0
    
    def empiler(self,x):
        (self.l).append(x)
    
    def depiler(self):
        return (self.l).pop()

    def affichage(self):
        print(self.l)

    def taille_pile(self):
        print(len(self.l))

#
    