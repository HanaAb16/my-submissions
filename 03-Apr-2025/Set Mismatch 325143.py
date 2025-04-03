# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if i != nums[i] - 1:
                if nums[i] != nums[nums[i] - 1]:
                    nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]
                else:
                    i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return [nums[i] , i + 1]