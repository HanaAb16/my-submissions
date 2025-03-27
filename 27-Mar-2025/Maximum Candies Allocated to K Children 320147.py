# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(candy):
            if candy == 0:
                return True

            child = 0  
            for pile in candies:
                    child += pile // candy
            return child >= k
        low = 0
        high = max(candies)
        while low <= high:
            mid = (high + low) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high

                
