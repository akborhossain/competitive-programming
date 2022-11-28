# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0;

        sumNode = ListNode()
        copyNode = sumNode

        # start iteration
        while (l1 != None or l2 != None or sum != 0):
            if l1 is not None:
                sum += l1.val;
                l1 = l1.next;

            if l2 is not None:
                sum += l2.val;
                l2 = l2.next;

            newNode = ListNode();
            newNode.val = sum % 10;
            copyNode.next = newNode;
            copyNode = newNode;

            sum = int(sum / 10);

        return sumNode.next;