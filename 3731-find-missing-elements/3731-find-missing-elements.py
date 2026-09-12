class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        list1=[i for i in range(min(nums),max(nums)+1)]
        list2= list(set(list1)-set(nums))
        list2.sort()
        return list2    
        