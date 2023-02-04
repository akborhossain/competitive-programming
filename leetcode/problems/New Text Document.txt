class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,h=1,num
        while l<=h:
            m= (l+h)//2
            var= m*m
            if var >num:
                h=m-1
            elif var<num:
                l=m+1
            else:
                return True
