class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        index= 0
        result= set()
        while (index < len(nums)-2):
            if nums[index] > 0:
                break
            right= len(nums)-1
            left= index+1
            while (left < right):
                if(nums[index]+nums[left]+nums[right] == 0):
                    result.add((nums[index], nums[left], nums[right]))
                    right-=1
                    left+=1
                elif (nums[index]+nums[left]+nums[right] > 0):
                    right-=1
                else:
                    left+=1
            j= index+1
            while (j < len(nums) and nums[index] == nums[j]):
                j+=1
            index=j
        return [list(e) for e in result]