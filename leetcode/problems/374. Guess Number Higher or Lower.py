class Solution:
    def guessNumber(self, n: int) -> int:
        l,h=1,n
        while True:
            m=(l+h)//2
            r= guess(m)
            if r>0:
                l=m+1
            elif r<0:
                h=m-1
            else:
                return m