class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        for i in range(len(haystack)-n+1):
            newString=haystack[i:i+n]
            if newString==needle:
                return i
        return -1
            