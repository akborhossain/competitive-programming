# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        previous, current=None, head
        while current:
            curr=current.next
            current.next=previous
            previous=current
            current=curr
        return previous