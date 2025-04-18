# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pos = 0
        dummy = ListNode(-1)
        tail = dummy
        l = head
        r = head
        while r:
            pos += 1
            if pos % k == 0:
                temp = l
                l = r.next
                r.next = tail
                tail = temp
                r = l
            else:
                r = r.next
        curr = tail.next
        tail.next = l
        while curr:
            temp = tail
            tail = curr
            curr = curr.next
            tail.next = temp
        return dummy.next