# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        rsum = 0
        maxsum = -inf
        for i in range(n):
            if rsum + nums[i] < nums[i]:
                rsum = nums[i]
            else:
                rsum += nums[i]
            maxsum = max(maxsum , rsum)
        return maxsum
