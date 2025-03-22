# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def recur(curr , path):
            nonlocal ans
            if not curr:
                return
            path += str(curr.val)
            if not curr.left and not curr.right:
                ans += int(path)
                return
            recur(curr.left , path)
            recur(curr.right , path)
            
        recur(root , '')
        return ans