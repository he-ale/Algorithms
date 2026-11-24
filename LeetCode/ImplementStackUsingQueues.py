from collections import deque

class MyStack:
    a: deque[int]
    b: deque[int]
    t: int

    def __init__(self):
        self.a= deque()
        self.b= deque()

    def push(self, x: int) -> None:
        self.a.append(x)
        self.t= x

    def pop(self) -> int:
        while (len(self.a)>1):
            aux= self.a.popleft()
            self.t= aux
            self.b.append(aux)
        e= None
        if(len(self.a)>0):
            e= self.a.popleft()
            self.a, self.b= self.b, deque()
        return e
        

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.a)==len(self.b)==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()