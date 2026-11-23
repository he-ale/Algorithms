class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary= dict()
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return [dictionary[nums[i]], i]

            dictionary[target-nums[i]]= i
        return []