def mult(x: int, y: int) -> int:
    res = 0
    for i in range(y):
        res += x
    return res

print(mult(7,5))

def mult2(x:int, y:int) -> int:
    res = 0
    
    if x<0 and y<0:
        res = mult(-x,-y)
    elif x<0:
        res = -mult(-x,y)
    elif y<0:
        res = -mult(x, -y)
    else:
        res = mult(x,y)
    
    return res

print(mult2(-7,5))
