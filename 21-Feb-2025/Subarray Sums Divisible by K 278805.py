# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        psum = 0
        ans = 0
        for i in range(len(nums)):
            psum += nums[i]
            ans += count[psum % k]
            count[psum % k] += 1
        return ans