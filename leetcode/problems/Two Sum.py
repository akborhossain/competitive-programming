class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=[]
        for x in range(0,n,1):
            c=0
            d=-1
            for y in range(n-1,x,d):
                if nums[x]+nums[y]==target:
                    l.append(x)
                    l.append(y)
                    c=c+1
                    break
            if c==1:
                break
        return l