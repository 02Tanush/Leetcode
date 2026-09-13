class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=0
        right=sum(nums)
        ans=[]

        for i in nums:
            right-=i
            ans.append(abs(left_sum-right))
            left_sum+=i
        return ans

        
        