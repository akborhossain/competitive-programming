class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        isnagetive=False
        
        if x<0:
           isnagetive=True
           x=-x 
        while x:
            rev=rev*10+x%10
            x//=10
        if rev <= (-2**31) or rev>=(2**31)-1:
            return 0
        return -rev if isnagetive else rev 
