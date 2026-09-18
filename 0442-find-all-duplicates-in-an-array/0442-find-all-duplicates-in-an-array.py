class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:       
        s = set()
        l = []
        
        for i in nums:
            if i in s:
                l.append(i)
            else:
                s.add(i)
                
        return l

        