class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if (len(nums) == 0):
            return 0
        setAux= set(nums)
        nums= list(setAux)
        nums.sort()
        j= 0
        maxLen= 1
        auxLen= 1 
        for i in range(1, len(nums)):
            if (nums[j]+1 == nums[i]):
                auxLen+= 1
            else:
                maxLen= max(maxLen, auxLen)
                auxLen= 1
            j+=1
        return max(maxLen, auxLen)
        