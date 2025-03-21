# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recur(curr , mn , mx):
            if not curr:
                return abs(mx - mn)

            return max(recur(curr.left , min(curr.val , mn) , max(curr.val , mx)) , recur(curr.right , min(curr.val , mn) , max(curr.val , mx)))
            
        return recur(root , root.val , root.val)