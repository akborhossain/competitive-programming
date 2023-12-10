class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        scount={}
        tcount={}
        for i in t:
            tcount[i]=1 + tcount.get(i, 0)

        h,n=0,len(tcount)
        l=0
        res,reslen=[-1,-1],float('inf')

        for i in range(len(s)):

            if s[i] in tcount:
                scount[s[i]] = 1+ scount.get(s[i],0)

            if s[i] in tcount and scount[s[i]]==tcount[s[i]]:
                h+=1

            while h==n:
                if (i-l+1)<reslen:
                    res=[l,i]
                    reslen=(i-l+1)
                if s[l] in scount:
                    scount[s[l]]-=1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    h-=1
                    
                l+=1
        l,r=res


        return s[l:r+1] if reslen!=float('inf') else ""