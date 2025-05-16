# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int: 
        l = 0
        check = nums[0]
        length = 1
        for r in range(1 , len(nums)):
            if (nums[r] & check):
                while l <= r and check & nums[r]:
                    check ^= nums[l]
                    l += 1
            length = max(length , r - l + 1)
            check |= nums[r]
        return length
                




        