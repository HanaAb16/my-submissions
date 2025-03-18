# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        level = defaultdict(list)
        def largest(curr , depth):
            if not curr:
                return
            level[depth].append(curr.val)
            largest(curr.left , depth + 1)
            largest(curr.right , depth + 1)
        largest(root , 0)
        ans = []
        for val in level.values():
            ans.append(max(val))
        return ans