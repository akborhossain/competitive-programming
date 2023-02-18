class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x,n=0,len(nums)
        while x<=n:
            if x not in nums:
                return x
            x+=1