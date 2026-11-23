

def quickSort(ls: list[int], l, r):
    if(l+1<r):
        p= partition(ls, l, r)
        quickSort(ls, l, p)
        quickSort(ls, p+1, r)

def partition(ls: list[int], l, r):
    pivot= ls[r-1]
    i= l
    for j in range(l, r-1):
        if (ls[j] <= pivot):
            ls[i], ls[j]= ls[j], ls[i]
            i+=1
    ls[i], ls[r - 1] = ls[r - 1], ls[i]
    return i

ls= [5, 2, 4, 7, 1, 3, 2, 6]
quickSort(ls, 0, len(ls))
print(ls)

