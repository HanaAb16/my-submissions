# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rcount , lcount = 0 , 0
        max_str = 0
        for r in range(len(s)):
            if s[r] == 'R':
                rcount += 1
            else:
                lcount += 1
            if lcount == rcount:
                max_str += 1
                lcount , rcount = 0 , 0
        return max_str
                
        