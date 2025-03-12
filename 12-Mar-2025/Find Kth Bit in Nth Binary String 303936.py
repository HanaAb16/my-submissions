# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def nth(n):
            if n == 1:
                return '0'
            ans = nth(n - 1)
            half = ''
            for i in ans:
                if i == '0':
                    half += '1'
                else:
                    half += '0' 
            return ans + '1'+ half[::-1]
        return nth(n)[k - 1]