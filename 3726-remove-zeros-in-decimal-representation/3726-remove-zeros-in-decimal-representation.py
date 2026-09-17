class Solution:
    def removeZeros(self, n: int) -> int:
        word=""
        for i in str(n):
            if i!='0':
                word+=i
        return int(word)       