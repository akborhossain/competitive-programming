class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newString=s.strip().split(" ")
        n=len(newString)
        return len(newString[n-1])