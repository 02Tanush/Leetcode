class Solution:
    def isBalanced(self, num: str) -> bool:
        count=0
        even=0
        odd=0
        for i in num:
            if count%2==0:
                even+=int(i)
                count+=1
            else:
                odd+=int(i)    
                count+=1
        if even==odd:
            return True
        else:
            return False    