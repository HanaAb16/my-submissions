# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        prefix = [nums[0]]
        for i in range(1 , len(nums)):
            if nums[i] < prefix[-1]:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1])
        stk = [nums[-1]]
        for i in range(len(nums) - 2 , 0 , -1):
            while stk and stk[-1] <= prefix[i - 1]:
                stk.pop()
            
            if stk and prefix[i - 1] < stk[-1] < nums[i]:
                return True
            stk.append(nums[i])
        return False

