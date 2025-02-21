# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dhead = ListNode(-1)
        dhead.next = head
        curr = dhead
        move = 0
        while move < n:
            curr = curr.next
            move += 1
        rem = dhead
        prev = None
        while curr:
            curr = curr.next
            prev = rem
            rem = rem.next
        if rem:
            prev.next = rem.next
        return dhead.next
        
