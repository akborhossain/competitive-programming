class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,h=1,n
        res=0
        while l<=h:
            m=(l+h)//2
            summation=(m*(m+1))//2
            if summation>n:
                h=m-1
            else:
                l=m+1
                res=max(res,m)
        return res
