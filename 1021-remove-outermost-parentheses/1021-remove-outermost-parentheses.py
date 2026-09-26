class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l=[]
        opened=0
        for char in s:
            if char=='(':
                if opened>0:
                    l.append(char)
                opened+=1
            else:
                opened-=1
                if opened>0:
                    l.append(char)
        return "".join(l)
        