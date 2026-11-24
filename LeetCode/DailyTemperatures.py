class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack= [0]
        report=[0]*len(temperatures)
        for i in range(1, len(temperatures)):
            while(len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]):
                aux=stack.pop()
                report[aux]= i-aux
            stack.append(i)
        return report