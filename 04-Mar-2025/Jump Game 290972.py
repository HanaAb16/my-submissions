# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        step = 0
        for i in range(len(nums) - 1):
            step = max(step , nums[i] + i)
            if step > i:
                continue
            else:
                return False
        return True
            
        