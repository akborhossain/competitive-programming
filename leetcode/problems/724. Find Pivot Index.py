class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        l=0
        for i,n in enumerate(nums):
            if total-l-n == l:
                return i
            l+=n
        return -1