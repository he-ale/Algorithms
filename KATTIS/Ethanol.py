
def solve(c: int):
    line1= '  '
    line2= '  '
    line3= 'H-'
    for i in range(c):
        line1+= 'H '
        line2+= '| '
        line3+= 'C-'
    print(line1)
    print(line2)
    print(line3+'OH')
    print(line2)
    print(line1)
    

if __name__ == "__main__":
    c= int(input())
    solve(c)