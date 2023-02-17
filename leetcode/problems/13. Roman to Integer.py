class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        sarray={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev=0
        for x in range(len(s)-1,-1,-1):
            if sarray[s[x]]<prev:
                sum-=sarray[s[x]]
            else:
                sum+=sarray[s[x]]
            prev=sarray[s[x]]
        
       
        return sum
            