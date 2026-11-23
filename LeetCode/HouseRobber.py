class Solution:
    def rob(self, nums: list[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        elif (len(nums) == 2):
            return max(nums[0], nums[1])

        result= [0]*len(nums)
        result[0]= nums[0]
        result[1]= nums[1]
        result[2]= nums[2] + nums[0]
        maximun= max(result[1], result[2])
        for i in range(3, len(nums)):
            aux= max(result[i-2], result[i-3])
            result[i]= nums[i] + aux
            maximun= max(result[i], maximun)
        return maximun

s= Solution()
print(s.rob(nums = [1, 2, 3, 1]))
print(s.rob(nums = [2, 7, 9, 3, 1]))
print(s.rob(nums = [2, 1, 1, 2]))