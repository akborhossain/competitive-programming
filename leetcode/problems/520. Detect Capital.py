class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n =len(word)
        count=0
        counthelp=0
        if n==1 :
            return True
        
        else:
            for x in word:
                if ord(x)>=65 and ord(x)<=90:
                    count=count+1
                else:
                    counthelp=counthelp+1
            if count==0 and counthelp!=n:
                return False
            elif count==1:
                for x in word:
                    if ord(x)>=65 and ord(x)<=90:
                        return True
                    else:
                        return False
            elif count==n or counthelp==n:
                return True
            else :
                return False
                    
        
        