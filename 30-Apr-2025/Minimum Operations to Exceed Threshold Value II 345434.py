# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums[0] < k:
            mini = heappop(nums)
            maxi = heappop(nums)
            heappush(nums , mini * 2 + maxi)
            ans += 1
        return ans
