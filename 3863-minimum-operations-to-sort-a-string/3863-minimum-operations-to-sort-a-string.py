class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # 0 operations: already sorted
        if list(s) == sorted(s):
            return 0
        
        # Length 2 and not sorted -> impossible (proper substrings have length 1)
        if n == 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        # 1 operation: prefix s[:-1] or suffix s[1:]
        if max(s[:-1]) <= s[-1] or s[0] <= min(s[1:]):
            return 1
        
        # 3 operations: max is stuck at front AND min is stuck at back
        if s[0] == max_char and s[-1] == min_char and s.count(max_char) == 1 and s.count(min_char) == 1:
            return 3
            
        return 2