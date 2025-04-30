# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.heap = []
        for i in range(1 , n + 1):
            self.heap.append(i)
        heapify(self.heap)

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap , seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)