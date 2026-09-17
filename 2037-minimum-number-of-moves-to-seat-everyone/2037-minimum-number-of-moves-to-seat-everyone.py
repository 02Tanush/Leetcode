class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sums=0
        for i in range(len(seats)):
            sums+=abs(seats[i]-students[i])
        return sums    

        