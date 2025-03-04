# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        ones = c["1"]
        s = list(s)
        l , r = 0 , 0
        
        while ones > 1 and l < len(s) and r < len(s):
            if s[l] == '0':
                if s[r] == '1':
                    s[l] , s[r] = s[r] , s[l]
                    l += 1
                    ones -= 1
            else:
                ones -= 1
                l += 1
            r += 1
        while r < len(s):
            if s[r] == '1':
                s[r] , s[len(s) - 1] = s[len(s) - 1] , s[r]
                break
            r += 1
        return ''.join(s)