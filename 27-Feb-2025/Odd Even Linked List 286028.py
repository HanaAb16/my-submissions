# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        odd = ListNode()
        ocurr = odd
        ecurr = even
        curr = head
        i = 1
        while curr:
            if i % 2 == 0:
                ecurr.next = curr
                ecurr = ecurr.next
            else:
                ocurr.next = curr
                ocurr = ocurr.next
            curr = curr.next
            i += 1
        ecurr.next = None
        ocurr.next = even.next
        
        return odd.next
          

        