class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)-1
        n=len(nums)
        while l<=h:
            m=(l+h)//2
            if nums[m]>target:
                h=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
               
        return l