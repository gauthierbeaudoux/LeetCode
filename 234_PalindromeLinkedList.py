# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        
        for i in range(len(result)//2):
            if result[i] != result[-1-i]:
                return False
            
        return True