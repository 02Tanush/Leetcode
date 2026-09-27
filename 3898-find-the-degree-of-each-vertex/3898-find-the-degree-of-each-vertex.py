class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for row in matrix:
            ans.append(sum(row))  # Each '1' represents a connected edge
        return ans

        