# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(n1 , n2 , level):
            if not n1 and not n2:
                return 
            if level % 2 != 0:
                n1.val , n2.val = n2.val , n1.val
                
            swap(n1.left , n2.right , level + 1)
            swap(n1.right , n2.left , level + 1)
            
        swap(root.left , root.right , 1)
        return root