class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashText=Counter(text)
        hashBalloon=Counter("balloon")
        res=float("inf")
        for c in hashBalloon:
            res=min(res, hashText[c] // hashBalloon[c])
        return res