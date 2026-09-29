class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
                if queryTime>=startTime[i] and queryTime<=endTime[i]:
                    count+=1
        return count