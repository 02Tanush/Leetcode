class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_num = -1
        
        for i in s.split():
            if i.isdigit():
                curr_num = int(i)
                if curr_num <= prev_num:
                    return False
                prev_num = curr_num
                
        return True   

        