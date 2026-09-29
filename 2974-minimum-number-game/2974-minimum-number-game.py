class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        while len(nums)!=0:
            a=nums.pop(0)
            arr.append(nums.pop(0))
            arr.append(a)
        return arr
        