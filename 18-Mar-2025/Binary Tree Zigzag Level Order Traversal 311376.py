# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
        def zigzag(curr , depth):
            if not curr:
                return 
            level[depth].append(curr.val)
            zigzag(curr.left , depth + 1)
            zigzag(curr.right, depth + 1)
        zigzag(root , 0)
        ans = []
        for key , val in level.items():
            if key % 2 == 0:
                ans.append(val)
            else:
                ans.append(list(reversed(val)))
        return ans
                