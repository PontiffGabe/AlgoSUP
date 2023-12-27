"""
exo 3.1, search in a sorted list
"""




"""
exo 3.2, sorted
"""

def is_sorted(l:list) -> bool:
    sorted = True
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            sorted = False
    return sorted

"""
exo 3.3
"""

def minimum(l:list, d: int, f: int) -> int:
    i_min = d

    while d < f:
        if l[i_min] > l[d+1]:
            i_min = d+1
        d+=1

    return i_min

print(minimum([4, -5, 3, -3, 8, -2, 0, 3, -6, 7], 2, 7))

def selection_sort(l: list) -> list:
    for i in range(len(l)):
        l[i] = l[minimum(l, i, len(l)-1)]
    return l

print(selection_sort([4 , -5 , 3 , -3 , 8 , 2 , 0 , 3 , -6 , 7]))