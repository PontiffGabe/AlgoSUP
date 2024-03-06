class Noeud:
    def __init__(self, valeur, sag = None, sad = None):
        self.valeur = valeur
        self.sag = sag
        self.sad = sad



if __name__ == '__main__':
    """
### ARBRE 1 : "Joli"
    1
   / \ 
  4   2
 / \   \ 
9   6   9
### CODE

    n4 = Noeud(9)
    n5 = Noeud(6)
    n7 = Noeud(9)

    n3 = Noeud(2, None, n7)
    n2 = Noeud(4, n4, n5)

    abr = Noeud(1, n2, n3)

    """
# ---------------------------
    """
### ARBRE 2 : "Shlong"
    1
   / \ 
  4   2
       \ 
        8
       / \ 
      5   7
### CODE

    n15 = Noeud(7)
    n14 = Noeud(5)
    
    n7 = Noeud(8, n14, n15)

    n3 = Noeud(2, None, n7)
    n2 = Noeud(4)

    abr = Noeud(1, n2, n3)

    """
# ---------------------------
    """
### ARBRE 3 : "Shlong Filiforme"
    1
     \ 
      2
     / \ 
    5   8
       / \ 
      4   7
         /
        9
### CODE

    n30 = Noeud(9)

    n15 = Noeud(7, n30)
    n14 = Noeud(4)

    n7 = Noeud(8, n14, n15)
    n6 = Noeud(5)

    n3 = Noeud(2, n6, n7)

    abr = Noeud(1, None, n3)

    """