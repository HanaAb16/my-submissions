# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        r1 , r2 = 0 , 0
        if len(nums1) % 2 != 0:
            for num in nums2:
                r1 ^= num
        if len(nums2) % 2 != 0:
            for num in nums1:
                r2 ^= num
        return r1 ^ r2
         