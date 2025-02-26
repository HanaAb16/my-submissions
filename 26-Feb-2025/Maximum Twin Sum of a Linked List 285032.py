# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        i = 0
        l = None
        r = head
        while i < n / 2:
            temp = r.next
            r.next = l
            l = r
            r = temp
            i += 1
        max_sum = 0
        while l:
            max_sum = max( max_sum , l.val + r.val)
            l = l.next
            r = r.next
        return max_sum

