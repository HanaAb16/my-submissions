# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(path , i):
            if len(path) == len(s):
                ans.append(path)
                return
            else:
                if s[i].isalpha():
                    backtrack(path + s[i].swapcase() , i + 1)
                backtrack(path + s[i] , i + 1)
        backtrack("" , 0)
        return ans
        