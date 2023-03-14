class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.valid(s[l]):
                l+=1
            while r>l and not self.valid(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            r-=1
            l+=1
        return True

    def valid(self,c):
        return (ord('A')<= ord(c) <=ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
          ord('0')<= ord(c) <=ord('9'))