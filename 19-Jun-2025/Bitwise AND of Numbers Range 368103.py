# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count


        for i in range(32):
            if (left & (1 << i)) and (right < left + (2 ** i)):
                    return left & ~((1 << i) - 1)                   
        return 0
        