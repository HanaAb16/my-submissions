# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor > 0:
            if xor % 2 != 0:
                ans += 1
            xor = xor >> 1
        return ans 
