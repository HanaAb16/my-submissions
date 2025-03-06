# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        solved = defaultdict(lambda: -1)
        stk = []
        ans = []
        for num in nums2:
            while stk and num > stk[-1]:
                solved[stk[-1]] = num
                stk.pop()
            stk.append(num)
        for num in nums1:
            ans.append(solved[num])
        return ans