# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = inf
        while low <= high:
            mid = (high + low) // 2
            ans = min(nums[mid], ans)

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return ans
                 