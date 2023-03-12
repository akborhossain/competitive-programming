class Solution:
    def countBits(self, n: int) -> List[int]:
        pd=[0]*(n+1)
        opset=1
        for i in range(1,n+1):
            if opset*2==i:
                opset=i
            pd[i]=1+pd[i-opset]
        return pd