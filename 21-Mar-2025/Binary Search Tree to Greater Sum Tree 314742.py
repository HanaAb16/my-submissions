# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(node , curr_sum):
            if not node:
                return 0
            right = recur(node.right , curr_sum)
            temp = node.val
            node.val += curr_sum + right
            left = recur(node.left , node.val)
            return left + right + temp
        recur(root , 0)
        return root
           