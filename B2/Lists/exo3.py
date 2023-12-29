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
exo 3.3, selection sort
"""

def minimum(l: list, d:int, f:int) -> int:
    i_min = d
    for i in range(d, f+1):
        if l[i_min] > l[i]:
            i_min = i
    return i_min


def select_sort(l: list) -> list:
    
    for i in range(len(l)):
        i_min = minimum(l, i, len(l)-1)
        l[i], l[i_min] = l[i_min], l[i]
    return l



print(minimum([-3,-2,-1,0,1,2,3], 0, 6))
print(select_sort([-3,-2,-1,0,1,2,3]))



"""
exo 3.4, insertion sort
"""

def insert_sort(l:list):
    for i in range(len(l)):
        j = i
        while j>0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1
    return l

a = [3,6,1,9,2,2, 9]
insert_sort(a)
print(a)

"""
exo 4.1, binary search
"""

def binary_search(l: list, x:int) -> int:

    left = 0
    right = len(l)-1

    while left <= right:
        middle = (left+right)//2
        if l[middle] == x:
            return middle
        elif l[middle] < x:
            left = middle + 1
        else:
            right = middle -1
    return -1




