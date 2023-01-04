class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        isNagetive=1
        if not s:
            return 0
        i,digit=0,0
        if s[i]=="-":
            isNagetive=-1
            i+=1
        elif s[i]=="+":
            i+=1
        while i<len(s):
            if s[i].isdigit():
                digit=digit*10+int(s[i])
            else:
                break
            i+=1
        digit=digit*isNagetive
        if digit > (2**31)-1:
            return (2**31)-1
        elif digit< -2**31:
            return -2**31
        else:
            return digit
        