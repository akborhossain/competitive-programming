class Solution:
    def reverseWords(self, s: str) -> str:
        sword=s.split(" ")
        j,m=0,len(sword)
        s=""
        for x in sword:
            n=len(x)
            j+=1

            for i in range(n-1,-1,-1):
                s+=x[i]
            if j!=m:
                s+=" "
        return s

#best solution

class Solution:
    def reverseWords(self, s: str) -> str:
        sword=s.split(" ")
        n=len(sword)
        for i in range(n):
            sword[i]=sword[i][::-1]
        return ' '.join(sword)
