class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() 
        
        while n != 1 and n not in seen:
            seen.add(n)
            
            nums = str(n)
            temp_sum = 0 
            
            for i in range(len(nums)):
                temp_sum += int(nums[i])**2 
            
            
            n = temp_sum 
            
        return n == 1
            
        