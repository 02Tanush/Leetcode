class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        word=str(n)
        sums=0
        product=1
        for i in word:
            product*=int(i)
            sums+=int(i)
        return product-sums    
        