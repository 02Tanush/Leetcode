class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        current_level = {s}
        
        while True:
            valid_strings = list(filter(is_valid, current_level))
            
            if valid_strings:
                return valid_strings
            
            next_level = set()
            for string in current_level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            
            current_level = next_level