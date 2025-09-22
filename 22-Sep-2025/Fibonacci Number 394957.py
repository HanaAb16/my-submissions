# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        m = {}                                     
        def f(i):
            if i == 0 or i == 1:
                return i
            if i not in m:
                m[i] = f(i - 1) + f(i - 2)
            return m[i]
        return f(n)


        