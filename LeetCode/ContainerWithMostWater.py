class Solution:
    def maxArea(self, height: list[int]) -> int:
        left= 0
        right= len(height)-1
        maximunAmount= 0
        while (left < right):
            w= right-left
            if(height[left] < height[right]):
                h= height[left]
                left+= 1
            else:
                h= height[right]
                right-= 1
            maximunAmount= max(h*w, maximunAmount)
        return maximunAmount
