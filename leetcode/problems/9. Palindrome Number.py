class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            n,tem=x,0
            while x!=0:
                tem=(tem*10)+(x%10)
                x=x//10
            if tem==n:
                return True
            if tem!=n:
                return False
