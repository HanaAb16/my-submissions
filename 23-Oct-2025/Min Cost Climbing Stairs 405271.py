# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(cost):
                return 0
            if i not in memo:
                memo[i] = min(dp(i + 1) , dp(i + 2)) + cost[i]
            return memo[i]
        return min(dp(0) , dp(1))