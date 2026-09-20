class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((122 - ord(char) + 1) * (i + 1) for i, char in enumerate(s))