class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1=-1
        for i in sentences:
            list1=i.split()
            if max1<=len(list1):
                max1=len(list1)
        return max1        
        