# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            temp = []
            for j in range(0 , 32):
                if i & (1 << j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans