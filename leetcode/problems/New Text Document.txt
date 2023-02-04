class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        subarray=0
        for n in nums:
            if subarray<0:
                subarray=0
            subarray+=n
            
            sum=max(sum,subarray)
        return sum