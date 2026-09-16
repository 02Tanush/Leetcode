class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        max_score = -1
        best_divisor = float('inf')

        for d in divisors:

            current_score = sum(1 for num in nums if num % d == 0)
            
            if current_score > max_score:
                max_score = current_score
                best_divisor = d
            
            elif current_score == max_score:
                best_divisor = min(best_divisor, d)

        return best_divisor