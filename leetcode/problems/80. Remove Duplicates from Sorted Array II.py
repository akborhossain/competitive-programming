class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2: return n
        j=1
        for i in range(2,n):
            if nums[i]!=nums[j-1]:
                j=j+1
                nums[j]=nums[i]
        return j+1


