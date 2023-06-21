class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        strnum=[]
        c=0
        s=""

        for i in nums:
            if c==0 :
                s+=str(i)
                c=1
            if i+1 not in nums:
                if str(i) not in s:
                    s+="->"+str(i)
                c=0
                strnum.append(s)
                s=""
        return strnum