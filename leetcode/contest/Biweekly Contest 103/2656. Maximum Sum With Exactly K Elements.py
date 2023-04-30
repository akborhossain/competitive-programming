class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_index=nums.index(max(nums))
        sum=0
        for i in range(k):
            sum+=nums[max_index]
            nums[max_index]+=1
        return sum