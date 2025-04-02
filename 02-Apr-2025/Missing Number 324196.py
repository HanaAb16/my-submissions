# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_dict = {num:num for num in nums}
        for i in range(len(nums)+1):
            if i not in my_dict:
                return i