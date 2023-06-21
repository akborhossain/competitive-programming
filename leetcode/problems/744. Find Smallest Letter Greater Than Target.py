class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if ord(target)>=ord(c):
                continue
            elif ord(target)<ord(c):
                return c
        return letters[0]
        