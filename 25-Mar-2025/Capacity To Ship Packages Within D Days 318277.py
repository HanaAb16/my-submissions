# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(capacity):
            day_count = 1
            curr_sum = 0
            for weight in weights:
                if curr_sum + weight > capacity:
                    day_count += 1
                    curr_sum = weight
                else:
                    curr_sum += weight
            return day_count <= days
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low