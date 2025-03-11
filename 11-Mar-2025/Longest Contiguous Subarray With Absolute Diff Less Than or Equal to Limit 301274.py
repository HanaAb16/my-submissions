# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque()
        mind = deque()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while maxd and nums[r] > maxd[-1]:
                maxd.pop()
            maxd.append(nums[r])
            while mind and nums[r] < mind[-1]:
                mind.pop()
            mind.append(nums[r])
            
            while mind and maxd and maxd[0] - mind[0] > limit:
                if nums[l] == maxd[0]:
                    maxd.popleft() 
                if nums[l] == mind[0]:
                    mind.popleft()
                
                l += 1
            ans = max(ans , r - l + 1)
        return ans
                