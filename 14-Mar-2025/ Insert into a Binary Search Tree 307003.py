# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new = TreeNode(val)
            root = new
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left , val)
            else:
                new = TreeNode(val)
                root.left = new
        if val > root.val:
            if root.right:
                self.insertIntoBST(root.right , val)
            else:
                new = TreeNode(val)
                root.right = new
        return root
