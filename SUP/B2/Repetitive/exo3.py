def exp(x:float, n:int) -> float:
    res = 1

    for i in range(n):
        res *= x

    return res

print(exp(2,5))