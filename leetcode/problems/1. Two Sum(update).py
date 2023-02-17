class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)
        for x in range(r):
            for y in range(x+1,r,1):
                if nums[x]+nums[y]==target:
                    return {x,y}