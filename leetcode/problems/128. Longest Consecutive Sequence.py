class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        length=0
        for n in nums:
            if n-1 not in numSet:
                tem=0
                while (n+tem) in numSet:
                    tem+=1
                length=max(length,tem)
        return length