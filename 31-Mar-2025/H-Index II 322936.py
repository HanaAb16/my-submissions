# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def check(h):
            return citations[-h] >= h
        low = 0
        high = n 
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high