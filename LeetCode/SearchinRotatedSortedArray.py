class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i= len(nums)-1
        while (nums[0] > nums[i]):
            i-= 1
        if (i == len(nums)-1):
            return self.binarySearch(nums, target, 0, i)
        
        return max(self.binarySearch(nums, target, 0, i), self.binarySearch(nums, target, i+1, len(nums)-1))

    def binarySearch(self, nums: list[int], target: int, left: int, right: int) -> int:
        while (left <= right):
            mid= (left+right)//2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                left= mid+1
            else:
                right= mid-1
        return -1
