# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap , (lists[i].val , i , lists[i]))
        ans = ListNode(-10001)
        curr = ans
        while heap:
            value , ind , node = heappop(heap)
            curr.next = node
            curr = curr.next
            if curr.next:
                heappush(heap , (curr.next.val , ind , curr.next))
        return ans.next
