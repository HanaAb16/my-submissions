# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost: cost[0] - cost[1])
        ans = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                ans += costs[i][0]
            else:
                ans += costs[i][1]
        return ans


             