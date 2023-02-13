# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=[]
        while head:
            temp.append(head.val)
            head=head.next
        l,h=0,len(temp)-1
        while l<=h:
            if temp[l]!=temp[h]:
                return False
            l+=1
            h-=1
        return True