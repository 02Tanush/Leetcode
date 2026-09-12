class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            if i.isdigit():
                ans+=i
            else:
                ans+="[.]"
        return ans
        