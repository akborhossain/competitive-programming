class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False
        return (len(set(pattern))==len(set(words))==len(set(zip(pattern, words))))

# update
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(words)!=len(pattern):
            return False
        charToword={}
        wordTochar={}
        for c,w in zip(pattern,words):
            if c in charToword and charToword[c]!=w:
                return False
            if w in wordTochar and wordTochar[w]!=c:
                return False
            charToword[c]=w
            wordTochar[w]=c
        return True
      
       

       