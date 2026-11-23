

def insertionSort(ls: list[int]):
    for i in range(1,len(ls)):
        key= ls[i]
        j= i-1
        while j>-1 and ls[j]>key:
            ls[j+1]= ls[j]
            j-=1
        ls[j+1]= key
        

ls= [5, 2, 4, 7, 1, 3, 2, 6]
insertionSort(ls)
print(ls)

