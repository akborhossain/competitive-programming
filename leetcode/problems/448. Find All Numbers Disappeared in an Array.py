class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        have=set(nums)
        n=len(nums)+1
        ans=[]
        for i in range(1,n):
            if i not in have:
                ans.append(i)
        return ans