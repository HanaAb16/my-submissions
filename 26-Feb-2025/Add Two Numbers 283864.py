# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i , j = l1 , l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while i and j:
            summ = carry + i.val + j.val
            curr.next = ListNode(summ % 10)
            curr = curr.next
            carry = summ // 10
            i = i.next
            j = j.next
        while i:
            summ = carry + i.val
            curr.next = ListNode(summ % 10)
            curr = curr.next
            carry = summ // 10
            i = i.next
        while j:
            summ = carry + j.val
            curr.next = ListNode(summ % 10)
            curr = curr.next
            carry = summ // 10
            j = j.next
        if carry:
            curr.next = ListNode(carry)
            



        return dummy.next

        