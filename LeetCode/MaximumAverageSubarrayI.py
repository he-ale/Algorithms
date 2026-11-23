class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currentSum= sum(nums[0:k])
        slow= 0
        maxSum= currentSum
        for fast in range(k, len(nums)):
            currentSum+= nums[fast]
            currentSum-= nums[slow]
            maxSum= max(currentSum, maxSum)
            slow+=1
        return maxSum/k