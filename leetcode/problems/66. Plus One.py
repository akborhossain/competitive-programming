class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        i,sum=0,0
        nums=[]

        while i<n:
            sum=(sum*10)+digits[i]
            i+=1
        sum+=1
        while sum>0:
            nums.append(sum%10)
            sum=sum//10
        nums.reverse()
        return nums