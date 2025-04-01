# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def check(radius):
            i , j = 0 , 0
            while i < len(houses):
                if abs(houses[i] - heaters[j]) <= radius:
                    i += 1
                else:
                    if j < len(heaters) - 1:
                        j += 1
                    else:
                        return False
            return True
        low = 0
        high = 10 ** 9
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

            
            