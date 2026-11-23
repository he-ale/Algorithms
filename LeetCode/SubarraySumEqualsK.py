class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        register= {0: 1}
        s= 0
        times= 0
        for num in nums:
            s+= num
            prefixSum= s - k

            times+= register.get(prefixSum, 0)
            register[s]= register.get(s, 0) + 1
        return times