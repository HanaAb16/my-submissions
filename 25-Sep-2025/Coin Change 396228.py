# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort(reverse = True)
        memo = {}
        def dp(i , c):
            if c == 0:
                return 0
            if i == n:
                return inf
            if (i , c) not in memo:
                include , exclude = inf , inf
                if coins[i] <= c:
                    include = 1 + dp(i , c - coins[i])
                exclude = dp(i + 1 , c)
                memo[(i , c)] = min(include , exclude)
            return memo[(i , c)]
        ans = dp(0 , amount)
        if ans == inf:
            return -1
        return ans
