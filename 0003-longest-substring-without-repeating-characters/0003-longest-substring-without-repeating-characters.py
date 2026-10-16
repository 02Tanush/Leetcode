class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If we've seen this character and it's inside our current window, move the left pointer
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
                
            # Update the latest index of the character
            char_map[current_char] = right
            
            # Calculate the max length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length