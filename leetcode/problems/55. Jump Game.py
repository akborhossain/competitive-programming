class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur=nums[0]
        for i in range(len(nums)):
            if cur>=len(nums)-1:
                return True
            if nums[i]==0 and cur==i:
                return False
            if cur<i+nums[i]:
                cur=nums[i]+i
        