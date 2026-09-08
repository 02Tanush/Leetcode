class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=""
        while n!=0:
            if n%2==0:
                binary+="0"
                n//=2
            else:
                binary+="1"
                n//=2
        actual_binary=binary
        for i in range(len(actual_binary)-1):
            if actual_binary[i]==actual_binary[i+1]:
                return False   
        return True                 
        