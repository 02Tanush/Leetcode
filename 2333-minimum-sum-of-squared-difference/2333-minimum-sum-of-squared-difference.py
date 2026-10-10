class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        k = k1 + k2
        
        if sum(diffs) <= k:
            return 0
            
        import collections
        counts = collections.Counter(diffs)
        
        # Filter out 0 differences and sort descending
        keys = sorted([key for key in counts.keys() if key > 0], reverse=True)
        
        # Append 0 to keys so the loop handles the last element properly
        keys.append(0)
        
        for i in range(len(keys) - 1):
            curr_diff = keys[i]
            next_diff = keys[i+1]
            count = counts[curr_diff]
            
            diff = curr_diff - next_diff
            
            if k >= count * diff:
                k -= count * diff
                counts[next_diff] += count
                counts[curr_diff] = 0
            else:
                q, r = divmod(k, count)
                counts[curr_diff] = 0
                counts[curr_diff - q] += (count - r)
                counts[curr_diff - q - 1] += r
                k = 0
                break
                
        ans = 0
        for diff, count in counts.items():
            if diff > 0:
                ans += count * (diff ** 2)
            
        return ans