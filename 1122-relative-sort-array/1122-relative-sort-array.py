class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list1=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    list1.append(j)           
        arr2_set = set(arr2)
        list2 = sorted([x for x in arr1 if x not in arr2_set])

        return list1 + list2