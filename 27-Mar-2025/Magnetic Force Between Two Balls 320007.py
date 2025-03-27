# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(distance):
            last = position[0]
            placed = 1
            for i in range(1 , len(position)):
                if position[i] - last >= distance:
                    last = position[i]
                    placed += 1
            return placed >= m
        low = 1
        high = max(position) - min(position)
        while low <= high:
            mid = (high + low) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high