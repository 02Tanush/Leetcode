class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sums=0
        for i,j in enumerate(nums,start=1):
            if len(nums)%i==0:
                sums+=j*j
        return sums        
        