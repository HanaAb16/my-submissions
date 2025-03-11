# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n == -1:
                return 1/x
            
            if n % 2 == 0:
                ans = power(n // 2)
                return ans * ans 
            else:
                ans = power(n // 2)
                return ans * ans * x 
        return power(n)