

def mergeSort(ls: list[int], l: int, r: int):
    if (l+1 < r):
        mid= (r+l)//2
        mergeSort(ls, l, mid)
        mergeSort(ls, mid, r)
        merge(ls, l, mid, r)

def merge(ls: list[int], l: int, m: int, r: int):
    left= ls[l:m]
    right= ls[m:r]
    left.append(float('inf'))
    right.append(float('inf'))
    i= 0
    j= 0
    for k in range(l, r):
        if (left[i]<=right[j]):
            ls[k]= left[i]
            i+=1
        else:
            ls[k]= right[j]
            j+=1

ls= [5, 2, 4, 7, 1, 3, 2, 6]
mergeSort(ls, 0, len(ls))
print(ls)

