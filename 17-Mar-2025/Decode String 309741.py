# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i] == ']':
                temp = ''
                while stk and stk[-1] != '[':
                    temp = stk.pop() + temp
                stk.pop()
                num = ''
                while stk and stk[-1].isnumeric():
                    num = stk.pop() + num
                stk.append(int(num) * temp)
            else:
                stk.append(s[i])
        return ''.join(stk)
        