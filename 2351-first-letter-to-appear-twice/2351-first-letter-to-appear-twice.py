class Solution:
    def repeatedCharacter(self, s: str) -> str:
        list1=[]
        for i in s:
            if i in list1:
                return i
            else:
                list1.append(i)

        