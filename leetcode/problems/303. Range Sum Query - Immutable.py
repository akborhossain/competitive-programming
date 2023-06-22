class NumArray:

    def __init__(self, nums: List[int]):

        self.prefix=[]
        c=0
        for i in nums:
            c+=i
            self.prefix.append(c)
        

    def sumRange(self, left: int, right: int) -> int:

        r=self.prefix[right]
        l=self.prefix[left-1] if left>0 else 0
        return r-l