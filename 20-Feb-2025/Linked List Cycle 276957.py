# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rab = head
        tor = head
        while rab and rab.next:
            rab = rab.next.next
            tor = tor.next
            if rab is tor:
                return True
        return False
            
