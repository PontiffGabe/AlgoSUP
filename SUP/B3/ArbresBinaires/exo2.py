from ArbreBinaire import Noeud
"""
Exo 2.1 DFS : Parcours profondeur (Depth-First Search)
"""

def afficher_arbre(abr: Noeud) -> str:
    if abr == None:
        return '_'
    else:
        return f"<{abr.valeur}, {afficher_arbre(abr.sag)}, {afficher_arbre(abr.sad)}>"




# welcome to my palace

n4 = Noeud(9)
n5 = Noeud(6)
n7 = Noeud(9)

n3 = Noeud(2, None, n7)
n2 = Noeud(4, n4, n5)

abr = Noeud(1, n2, n3)

print(afficher_arbre(abr))