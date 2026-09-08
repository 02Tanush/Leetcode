class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num != 0:
            if num % 2 == 0:
                binary += "1"   
            else:
                binary += "0"   
            num //= 2
        return int(binary[::-1], 2)