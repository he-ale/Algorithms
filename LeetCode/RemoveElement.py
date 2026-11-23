class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        j= 0
        for i in range(nums):
            if (nums[i]==val):
                nums[j]=nums[i]
            j+=1