class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x=sorted(nums1+nums2)
        n=len(x)
        if n%2==0:
            return float((x[n/2]+x[n/2-1]))/float(2)
        else:
            return x[n//2]    

        