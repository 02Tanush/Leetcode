class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        remainder=0
        for i in nums:
            if i%3!=0:
                remainder+=1
        return remainder        
        