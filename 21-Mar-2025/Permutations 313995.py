# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        def backtrack(path , visited):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    backtrack(path , visited)
                    visited.remove(path.pop())
            
        backtrack([] , visited)
        return ans