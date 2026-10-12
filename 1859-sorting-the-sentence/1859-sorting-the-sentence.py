class Solution:
    def sortSentence(self, s: str) -> str:
        arr=[]
        words=list(s.split())
        count=1
        i=0

        while i<len(words):
            if int(words[i][-1])==count:
                arr.append(words[i][:-1])
                count+=1
                i=0
            else:
                i+=1
        return " ".join(arr)
        