from collections import deque
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        indexes= deque()
        for i in range(len(nums)):
            if(nums[i] != 0):
                if(len(indexes) != 0):
                    j= indexes.popleft()
                    nums[j]= nums[i]
                    nums[i]= 0       
            else:
                indexes.append(i)
            
