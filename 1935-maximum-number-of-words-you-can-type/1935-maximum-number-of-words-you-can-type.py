class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        list1=text.split()
        count=0
        for i in list1:
            for j in range(len(brokenLetters)):
                if brokenLetters[j] in i:
                    count+=1
                    break
        return len(list1)-count            
        