# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i , cap):
            if cap == 0:
                return True
            if i >= len(nums):
                return False
            if (i , cap) not in memo:
                include = False
                if nums[i] <= cap:
                    include = dp(i + 1 , cap - nums[i])
                    if include:
                        return True 
                exclude = dp(i + 1 , cap)
                memo[(i , cap)] = include or exclude
            return memo[(i , cap)]
        tot = sum(nums)
        if tot % 2 == 0:
            return dp(0 , tot // 2)
        return False

        