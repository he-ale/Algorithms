class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current= nums[0]
        count= 1
        j= 1
        for i in range(1, len(nums)):
            if(nums[i]==current):
                if(count<2):
                    nums[j]= nums[i]
                    count+=1
                    j+=1
            elif(nums[i]!=current):
                current= nums[i]
                count=1
                nums[j]= nums[i]
                j+=1
        return j