# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def sub(idx , path):
            # if idx >= len(nums):
            #     ans.append(path.copy())
            #     return
            # sub(idx + 1 , path)
            # path.append(nums[idx])
            # sub(idx + 1 , path)
            # path.pop()
            
            ans.append(path.copy())
            for i in range(idx, len(nums)):
                path.append(nums[i])
                sub(i + 1 , path)
                path.pop() 
        sub(0 , [])
        return ans
            
