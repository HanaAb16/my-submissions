# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(path):
            if len(path) == n:
                ans.append(path)
                return
            if path and path[-1] == '0':
                backtrack(path + '1')
            else:
                backtrack(path + '0')
                backtrack(path + '1')
        backtrack('')
        return ans
