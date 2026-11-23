class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack= []
        for token in tokens:
            if token=='+' or token=='/' or token=='*' or token=='-':
                a= stack.pop()
                if (token == '+'):
                    stack[-1]= stack[-1]+a
                elif (token == '-'):
                    stack[-1]= stack[-1]-a
                elif (token == '/'):
                    if a < 0 and stack[-1]>=0:   
                        stack[-1]= -(stack[-1]//abs(a))
                    elif a > 0 and stack[-1]<0:   
                        stack[-1]= -(abs(stack[-1])//a)
                    else:
                        stack[-1]= stack[-1]//a
                else:
                    stack[-1]= stack[-1]*a
            else: 
                stack.append(int(token))
        return stack[-1]

s= Solution()
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])