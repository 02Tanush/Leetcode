class Solution:
    def reverseWords(self, s: str) -> str:
        text=s.split()
        text.reverse()
        word=""
        for i in text:
            word=word+i
            word=word+" "
        word2=word.strip()
        return word2
        