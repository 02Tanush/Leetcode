class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        diff=abs(max(nums)-min(nums))
        if diff<2*k:
            return 0
        else:
            return diff-2*k    
        