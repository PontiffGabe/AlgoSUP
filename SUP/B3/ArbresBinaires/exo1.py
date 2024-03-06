from ArbreBinaire import Noeud

"""
Exo 1.1: Taille (Size)

Axiome : taille(arbre_vide) = 0
[taille(noeud) = 1 + taille(sous_arbre_gauche) + taille(sous_arbre_droite)]
"""

def taille(abr : Noeud) -> int:
    if abr == None:
        return 0
    else:
        return 1 + taille(abr.sag) + taille(abr.sad)
    


"""
Exo 1.2: Hauteur (Height)
"""

def hauteur(abr: Noeud) -> int:
    if abr == None:
        return -1
    else:
        return 1 + max(hauteur(abr.sag), hauteur(abr.sad))
    

n4 = Noeud(9)
n5 = Noeud(6)
n7 = Noeud(9)

n3 = Noeud(2, None, n7)
n2 = Noeud(4, n4, n5)

abr = Noeud(1, n2, n3)

print(taille(abr))
print(hauteur(abr))