class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        left=0
        maxarea=-1
        while left<right:
            sortline= min(height[left], height[right])
            maxarea=max(maxarea,sortline*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        