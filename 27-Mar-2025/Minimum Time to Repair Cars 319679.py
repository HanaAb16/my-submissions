# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(minute):
            repaired = 0
            for r in ranks:
                repaired += floor(sqrt(minute / r))
            return repaired >= cars
        low = 1
        high = max(ranks) * (cars ** 2)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low