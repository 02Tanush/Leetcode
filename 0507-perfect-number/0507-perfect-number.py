class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sums=0
        if num==1:
            return False

        sums=1    
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sums+=i
                sums+=num//i
        if sums==num:
            return True
        else:
            return False    
        