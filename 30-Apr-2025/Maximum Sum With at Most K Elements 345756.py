# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        res = []
        for i in range(len(grid)):
            temp = []
            heapify(temp)
            for j in range(len(grid[0])):
                heappush(temp , grid[i][j])
                if len(temp) == limits[i] + 1:
                    heappop(temp)
            res.extend(temp)
        heapify(res)
        while len(res) > k:
            heappop(res)
        return sum(res)
