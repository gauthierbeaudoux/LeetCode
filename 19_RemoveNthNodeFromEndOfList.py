head = [1,2,3,4,5]
n = 2

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        longueur_liste = 1
        copy_node = head
        while copy_node.next != None:
            longueur_liste += 1
            copy_node = copy_node.next
        
        if longueur_liste == 1:
            return None
        a_supprimer = longueur_liste-n
        suivant = head
        i = 0
        while i < a_supprimer:
            precedent = suivant
            suivant = suivant.next
            i += 1
        
        if a_supprimer == 0:
            return head.next

        precedent.next = suivant.next
        return head