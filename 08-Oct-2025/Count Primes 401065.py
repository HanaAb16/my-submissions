# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        bucket = [0] * n
        ans = 0
        for i in range(2 , n):
            if not bucket[i]:
                ans += 1
                j = 2 * i
                while j < n:
                    bucket[j] = 1
                    j += i
            i += 1
        return ans
        

        