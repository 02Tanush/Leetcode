class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort1=sorted(heights)
        count=0
        for i in range(len(sort1)):
            if sort1[i]!=heights[i]:
                count+=1
        return count        
        