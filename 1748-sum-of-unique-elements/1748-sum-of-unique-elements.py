class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums.sort()
        list1=[]
        list2=[]
        for i in nums:
            if i in list1:
                list2.append(i)
            else:
                list1.append(i)
        list3=list(set(list2))
        for j in list3:
            list1.remove(j)
        return sum(i for i in list1)   
        