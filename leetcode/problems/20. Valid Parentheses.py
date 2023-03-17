class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for c in s:
            if c=='(' or c=='[' or c=='{':
                st.append(c)
            elif c==')' or c==']' or c=='}':
                if not st:
                    return False
                tem=st.pop()
                if (c==')' and tem!='(' ) or (c==']' and tem!='[') or (c=='}' and tem!='{'):
                    return False
        if st:
            return False
        return True