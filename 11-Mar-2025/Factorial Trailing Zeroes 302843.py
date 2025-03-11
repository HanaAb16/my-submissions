# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def fact(self, n):
        if n == 0:
            return 1
         
        return n * self.fact(n - 1)
    def trailingZeroes(self, n: int) -> int:
        ans = self.fact(n)
        count = 0
        while ans >= 10 and ans % 10 == 0:
            ans //= 10
            count += 1
        return count
        