# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        if length % 2 == 0:    
            fast = slow
        else:
            fast = slow.next
        slow = prev
        #print(slow.val , fast.val)
        while fast:
            if slow.val == fast.val:
                slow = slow.next
                fast = fast.next
            else:
                return False
        return True
    





    