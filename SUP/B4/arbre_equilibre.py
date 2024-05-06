def insertAVL(x,A):
    if A == None:
        return AVL(x,None,None,0) # x = val , fils gauche, fils droit, desequilibre
    elif x == A.key:
        return (A,False)
    elif x <= A.key:
        (A.left,dh) == insertAVL(x,A.left)
        if not dh:
            return (A,False)
        else:
            A.bal +=1 # A.bal desequilibre de A
        if A.bal == 2:
            if A.left.bal == 1:
                A == rr(A) # Right Rotation of A
            else:
                A = lrr(A) # Left Right Rotation of A
        return (A,A.bal == 1)
    else: #c'est moi qui ai supposé d'ecrire ce code, j'en sais rien du tout
        (A.left,dh) == insertAVL(x,A.right)
        if not dh:
            return (A,False)
        else:
            A.bal +=1 # A.bal desequilibre de A
        if A.bal == 2:
            if A.right.bal == 1:
                A == lr(A) # Left Rotation of A
            else:
                A = rlr(A) # Right Left Rotation of A
        return (A,A.bal == 1)
        
        
        
        
        
        
        
        

            