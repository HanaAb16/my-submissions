# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
                return head

        def split(root):
            slow = root
            fast = root.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid

        def merge(left , right):
            dummy = ListNode(0)
            tail = dummy
            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left if left else right
            return dummy.next
        
        mid = split(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left , right)
            