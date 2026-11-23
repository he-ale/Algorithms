class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies= dict()
        for num in nums:
            if num not in frequencies:
                frequencies[num]= 1
            else:
                frequencies[num]+= 1

        nums= list(frequencies.items())
        nums.sort(key=lambda x: x[1], reverse=True)

        nums= nums[0:k]

        rs= [k for (k,v) in nums]
        return rs