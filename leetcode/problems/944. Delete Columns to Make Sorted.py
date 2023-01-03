class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        strlen=len(strs[0])
        delet=0
        for x in range(0,strlen,1):
            for y in range(1,n):
                if strs[y-1][x]<=strs[y][x]:
                    continue
                else:
                    delet=delet+1
                    break
                
        return delet
