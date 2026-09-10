class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in nums:
            list1.append(i*i)
        list1.sort()
        return list1    
        