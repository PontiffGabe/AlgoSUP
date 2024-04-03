"""
TD ALGO 2.2
"""

#EXERCICE 1
"""
1.
a) premier element.
b) fils gauche : x2 ; fils droit : x2 + 1
c) division entiere : //2 
d) on prend la longueure du tableau et on verifie si ix2 et ix2+1 ne depasse pas la longueure du tableau ou si c'est None.

2. [5, 2, 12, -1, 0, 4, 1, 4, None, None, 11, None, ...]

3. def prefix(B):
       if B!= None: 
           print(B.key)
           prefix(B.key)
           prefix(B.right)

   def prefix(T, i=1):
       if i<len(T) and T[i] != None:
           print(T[i])
           prefix(T, 2*i)
           prefix(T,2*i+1)
"""

#EXERCICE 2

def size(T,i=1):
    if i > len(T) or T[i] != None :
        return 0
    else:
        return 1 +size(T,2*i) +size(T,2*i+1)

def hierfrombintree(B,n):
    T= []
    maxi = 2**n
    for _ in range(n):
        T.append(None)
    hierformbintree(B,T,maxi)
    return T

def hier2tree(L,i=1):
    if i>= len(L) or L[i] == None:
        return None
    else:
        B= bintree.BinTree(L[i],None,None)
        B.left = hier2tree(L,2*i)
        B.right = hier2tree(L, 2*i+1)
        return B
def hier2tree(L,i=1):
    if i >= len(L) or L[i] == None:
        return None
    else:
        return BinTree(T[i], treeFromHier2(T,2*i), treeFromHier2(T, 2*i+1)) 
