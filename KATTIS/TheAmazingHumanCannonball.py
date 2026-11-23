import math

def solve(v, theta, x, hMin, hMax):
    angle= (theta*math.pi)/180
    y= (x * math.tan(angle)) - (0.5 * 9.81 * (x / (v * math.cos(angle)))**2)
    result= 'Safe' if hMin+1<y<hMax-1 else 'Not Safe'
    print(result)
    return result
    

if __name__ == "__main__":
    n= int(input())
    for i in range(n):
        line= input().split(" ")
        v, theta, x, hMin, hMax= float(line[0]), float(line[1]), float(line[2]), float(line[3]), float(line[4])
        solve(v, theta, x, hMin, hMax)
