def max3(x: int, y: int, z: int) -> int:
    m = 0

    if x > y and x > z:
        m = x
    elif y > x and y > z:
        m = y
    else:
        m = z
        
    return m