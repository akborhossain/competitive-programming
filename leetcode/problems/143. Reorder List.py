class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Handle edge cases where the list is empty or has only one node
        if not head or not head.next:
            return
        
        # Find the middle node of the list using a slow and a fast pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge the two halves of the list by alternating between nodes
        p1 = head
        p2 = prev
        while p2.next:
            # Save the next node of p1 to a temporary variable
            temp = p1.next
            
            # Set the next nodes of p1 and p2
            p1.next = p2
            p2 = p2.next
            p1.next.next = temp
            
            # Move the pointers to the next nodes
            p1 = temp
        
        return