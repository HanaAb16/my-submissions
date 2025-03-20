# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(nums):
            n = len(nums)
            if n == 0:
                return None
            if n == 1:
                return TreeNode(nums[0])
            m = n // 2
            left = divide(nums[0:m])
            right = divide(nums[(m + 1):n])
            return TreeNode(nums[m] , left , right)
        return divide(nums)