from collections import deque
#this class implement file using the list object
class file:
    def __init__(self) :
        self.l=[]

    def file_vide(self):
        return len(self.l)==0
    
    def enfiler(self,x):
        (self.l).append(x)
    
    def defiler(self):
        if (not(self.file_vide())):
            return (self.l).pop(0)
        else:
            print("file vide")
            return None

    def affichage(self):
        print(self.l)

    def taille_file(self):
        print(len(self.l))

#this class implement file using the deque object
class filed:
    def __init__(self) :
        self.l=deque([])

    def file_vide(self):
        return len(self.l)==0
    
    def enfiler(self,x):
        (self.l).append(x)
    
    def defiler(self):
        if (not(self.file_vide())):
            return (self.l).popleft()
        else:
            print("file vide") 
    def affichage(self):
        print(self.l)

    def taille_file(self):
        print(len(self.l))

# p=filed()
# p.emfiler(45)
# p.emfiler(30)
# p.emfiler(5)
# p.affichage()
# p.taille_file()
# p.defiler()
# p.affichage()
        
# p=file()
# p.emfiler(23)
# p.emfiler(60)
# p.emfiler(9)
# p.affichage()
# p.taille_file()
# p.defiler()
# p.affichage()
    

