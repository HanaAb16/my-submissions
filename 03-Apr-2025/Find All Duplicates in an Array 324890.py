# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if i != nums[i] - 1:
                if nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]
                else:
                    i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(nums[i])
        return ans