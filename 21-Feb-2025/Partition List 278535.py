# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dhead = ListNode(-101)
        dhead.next = head
        left = dhead
        while left.next and left.next.val < x:
            left = left.next
        right = left.next
        while right and right.next:
            if right.next.val >= x:
                right = right.next
            else:
                temp = right.next
                right.next = right.next.next
                temp2 = left.next
                left.next = temp
                temp.next = temp2
                left = left.next
                right = left.next
        return dhead.next

                

        