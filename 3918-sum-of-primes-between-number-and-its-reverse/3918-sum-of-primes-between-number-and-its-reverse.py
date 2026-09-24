def is_prime(n):
    
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
            
    return n
            
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        m=int(str(n)[::-1])
        sums=0
        for i in range(min(m,n),max(m,n)+1):
            if is_prime(i) is False:
                continue
            else:
                sums+=i    
        return sums        

        