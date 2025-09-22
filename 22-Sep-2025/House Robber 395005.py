# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}
        def r(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i] , nums[i - 1])
            if i not in m: 
                m[i] = max(r(i - 1), r(i - 2) + nums[i])
            return m[i]
        return r(len(nums) - 1)