from ArbreBinaire import Noeud
"""
Exo 3.1 : Sérialisation
"""

def to_linear(B: Noeud) -> str:
    if B == None:
        return "()"
    else:
        return f"({B.valeur}" + to_linear(B.sag) + "" + to_linear(B.sad) + ")"
    

"""
Exo 3.2 : Longueurs de cheminement et Profondeurs moyennes
"""

def profondeur_moyenne(abr : Noeud) -> int:
    def calc_profondeur_moyenne(abr, profondeur):
        if abr == None:
            return 0, 0
        else:
            profg, nb_gauche = calc_profondeur_moyenne(abr.sag, profondeur + 1)
            profd, nb_droite = calc_profondeur_moyenne(abr.sad, profondeur + 1)

            prof_totale = profondeur + profg + profd
            nb_noeuds = 1 + nb_gauche + nb_droite

            return prof_totale, nb_noeuds
        
    prof_moyenne, nb_noeuds = calc_profondeur_moyenne(abr, 0)

    if nb_noeuds == 0:
        return 0
    else:
        return prof_moyenne/nb_noeuds


"""
Exo 3.3 : Longueurs de cheminement et Profondeurs moyennes
"""




n4 = Noeud(9)
n5 = Noeud(6)
n7 = Noeud(9)

n3 = Noeud(2, None, n7)
n2 = Noeud(4, n4, n5)

abr = Noeud(1, n2, n3)

print(to_linear(abr))
print(profondeur_moyenne(abr))