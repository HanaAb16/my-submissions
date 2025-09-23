# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = {}
        def dp(i):
            if i == len(nums):
                return 0
            if i not in m:
                m[i]=1
                for j in range(i + 1 , len(nums)):
                    if nums[j] > nums[i]:
                        m[i] = max(1 + dp(j) , m[i])
            return m[i]
        ans = 0
        for i in range(len(nums)):
            ans = max(dp(i) , ans)
        return ans
