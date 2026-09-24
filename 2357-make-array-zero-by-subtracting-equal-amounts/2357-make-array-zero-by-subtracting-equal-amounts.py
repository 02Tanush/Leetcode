class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        list1=[]
        for i in nums:
            if i==0:
                continue
            elif i in list1:
                continue
            else:
                list1.append(i)
        return len(list1)                