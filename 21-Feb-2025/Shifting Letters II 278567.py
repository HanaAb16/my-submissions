# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * len(s)
        new = ''
        for i in shifts:
            if i[2] == 0:
                pre[i[0]] -= 1
                if i[1] + 1 < len(pre):
                    pre[i[1] + 1] += 1
            else:
                pre[i[0]] += 1
                if i[1] + 1 < len(pre):
                    pre[i[1] + 1] -= 1
        for i in range(1 , len(pre)):
            pre[i] += pre[i - 1]
        for j in range(len(s)):
            new += chr(((ord(s[j]) - 97 + pre[j]) % 26) + 97)
        return new
