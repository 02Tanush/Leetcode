class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sums = sum(int(j) for j in str(nums[i]))
            if sums==i:
                return i
        return -1         
        