# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        direc = list(map(str , path.split("/")))
        print(direc)
        stk = []
        for pth in direc:
            if pth == '..':
                if stk:
                    stk.pop()
            elif pth == '.' or not pth:
                continue
            else:
                stk.append(pth)
        return '/' + '/'.join(stk)