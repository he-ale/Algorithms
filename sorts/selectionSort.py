

def selectionSort(ls: list[int]):
    for i in range(len(ls)-1):
        j= minIndex(ls, i)
        ls[j], ls[i]=ls[i], ls[j]

def minIndex(ls: list[int], i: int):
    for j in range(i+1, len(ls)):
        if(ls[j]<ls[i]):
            i= j
    return i

ls= [5, 2, 4, 7, 1, 3, 2, 6]
selectionSort(ls)
print(ls)

