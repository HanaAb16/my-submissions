# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if i != nums[i] - 1:
                if nums[i] != nums[nums[i] -1]:
                    nums[nums[i] -1] , nums[i] = nums[i] , nums[nums[i] -  1]
                else:
                    i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(i + 1)
        return ans