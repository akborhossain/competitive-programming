class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res=[]
        n=num//3
        for i in range(n-2,n+6,1):
            tem=0
            for j in range(0,3,1):
                tem+=(i+j)
            if tem==num:
                res.append(i)
                res.append(i+1)
                res.append(i+2)
                return res
        return res