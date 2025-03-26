# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def check(q):
            prefix  = [0] * len(nums)
            for i in range(q):
                prefix[queries[i][0]] += queries[i][2]
                if queries[i][1] + 1 < len(nums):
                    prefix[queries[i][1] + 1] -= queries[i][2]
            for i in range(1 , len(prefix)):
                prefix[i] += prefix[i - 1]
            for i in range(len(nums)):
                if nums[i] - prefix[i] > 0:
                    return False
            return True
        low = 0
        high = len(queries)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        if low <= len(queries):
            return low
        else:
            return -1
                
            
            
            

