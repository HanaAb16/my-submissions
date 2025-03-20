# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
                return None
            if key > root.val:
                root.right = self.deleteNode(root.right , key)
            elif key < root.val:
                root.left = self.deleteNode(root.left , key)
            else:
                if not root.left and not root.right:
                    root = None
                elif root.right and not root.left:
                    root = root.right
                elif root.left and not root.right:
                    root = root.left
                else:
                    curr = root.right
                    while curr.left:
                        curr = curr.left
                    root.val = curr.val
                    root.right = self.deleteNode(root.right , curr.val)
            return root

