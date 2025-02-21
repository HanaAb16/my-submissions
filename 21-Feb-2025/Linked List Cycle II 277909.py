# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tor = head
        rab = head
        while rab and rab.next:
            tor = tor.next
            rab = rab.next.next
            if rab is tor:
                break
        if not rab or not rab.next:
            return
        rab = head
        while rab is not tor:
            rab = rab.next
            tor = tor.next
        return rab
            
        
                
