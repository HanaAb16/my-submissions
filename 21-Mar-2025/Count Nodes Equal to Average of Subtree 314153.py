# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def recur(curr):
            nonlocal ans
            if not curr:
                return 0 , 0
                
            left , left_count = recur(curr.left)
            right , right_count = recur(curr.right)

            
            curr_sum = left + right + curr.val
            curr_count = left_count + right_count + 1

            if curr_sum // curr_count == curr.val:
                ans += 1
            return curr_sum , curr_count

        recur(root)
        return ans