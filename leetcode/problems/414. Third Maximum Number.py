class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num != first:
                third = second
                second = num
            elif num > third and num != second and num != first:
                third = num
        return third if third != float('-inf') else first