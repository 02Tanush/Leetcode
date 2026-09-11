class Solution:
    def scoreOfString(self, s: str) -> int:
        sums=0
        for i in range(len(s)-1):
            sums+=abs(ord(s[i+1])-ord(s[i]))
        return sums    