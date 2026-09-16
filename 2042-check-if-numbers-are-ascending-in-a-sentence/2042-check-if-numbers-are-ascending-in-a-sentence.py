class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_num = -1
        
        for token in s.split():
            if token.isdigit():
                curr_num = int(token)
                if curr_num <= prev_num:
                    return False
                prev_num = curr_num
                
        return True   

        