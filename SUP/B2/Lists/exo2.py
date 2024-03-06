"""
exo 2.1, build a list
"""

def temp(n:int, val:any) -> list:
    list = []

    for i in range(n):
        list.append(val)

    return list

"""
exo 2.2, histogram
"""

def histogram(s: str) -> list:
    list = temp(256, 0)
    for i in range(len(list)):
        for e in s:
            if e == chr(i):
                list[i] += 1

    return list

print(histogram("abcdefgabcdefg"))

def n_occ(l: list) -> int:
    n = 0
    for e in l:
        if e > 0:
            n+=1
    return n

print(n_occ(histogram("abcdabcd")))

def most_frequent(s: str) -> (int, chr):
    max, char = 0, chr(0)

    hist = histogram(s)

    for i in range(len(hist)):
        if hist[i] > max:
            max = hist[i]
            char = chr(i)

    return max, char


print(most_frequent("abcdabcd"))