class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=0
        left=0
        right=len(height)-1
        for i in range(right):
            width=right-left
            water=width*(min(height[left],height[right]))

            if water>max:
                max=water

            if height[left]>height[right]:
                right=right-1
            else:
                left=left+1        
        return max        
        