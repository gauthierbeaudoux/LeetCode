list1 = [10,1,13,6,9,5]
a = 3
b = 4
list2 = [1000000,1000001,1000002]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        head = list1
        while head:
            if i+1 == a:
                head_a = head
            elif i-1 == b:
                head_b = head
            head = head.next
            i += 1
        head_a.next = list2
        
        head2 = list2
        fini = True
        while fini:
            if head2.next == None:
                head2.next = head_b
                fini = False
            head2 = head2.next
        return list1