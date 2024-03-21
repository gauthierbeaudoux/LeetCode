head = [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        premier = True
        if not head or not head.next:
            return head
        
        while head.next:
            if premier:
                suivant = head.next
                avant = head
                head.next = None
                head = suivant
                premier = False
            else:
                suivant = head.next
                head.next = avant
                avant = head
                head = suivant
        
        head.next = avant
            
        return head
                