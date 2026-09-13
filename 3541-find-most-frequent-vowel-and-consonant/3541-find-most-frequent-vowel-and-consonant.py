class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        max_vowel=0
        max_consonant=0
        for i in set(s):
            char_count=s.count(i)

            if i in vowels:
                if char_count>max_vowel:
                    max_vowel=char_count
            else:
                if char_count > max_consonant:
                    max_consonant=char_count
        return max_vowel+max_consonant

        