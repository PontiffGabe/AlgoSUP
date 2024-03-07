from ArbreBinaire import Noeud
from collections import deque



"""
Exo 2.1 DFS : Parcours profondeur (Depth-First Search)
"""

def afficher_arbre(abr: Noeud) -> str:
    if abr == None:
        return '_'
    else:
        return f"<{abr.valeur}, {afficher_arbre(abr.sag)}, {afficher_arbre(abr.sad)}>"



"""
Exo 2.2 BFS : Parcours largeur (Breadth-First Search)
"""

def afficher_largeur_arbre(abr: Noeud) -> str:
    if abr == None:
        return ""
    else:
        res = ""

        file = deque([abr])

        while len(file) > 0:
            tmp = file.popleft()
            
            res += str(tmp.valeur)
            
            if tmp.sag != None:
                file.append(tmp.sag)
            if tmp.sad != None:
                file.append(tmp.sad)
            

        return res




n4 = Noeud(9)
n5 = Noeud(6)
n7 = Noeud(9)

n3 = Noeud(2, None, n7)
n2 = Noeud(4, n4, n5)

abr = Noeud(1, n2, n3)

print(afficher_arbre(abr))
print(afficher_largeur_arbre(abr))