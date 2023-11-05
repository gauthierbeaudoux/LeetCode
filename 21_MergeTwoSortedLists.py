# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def merge_two_list(list1, list2):
    result_list = ListNode()
    voyageur = result_list
    while not (list1 == None or list2 == None):
        if list1.val <= list2.val:
            voyageur.next = list1
            list1 = list1.next
        else:
            voyageur.next = list2
            list2 = list2.next
        voyageur = voyageur.next
    
    if list1 == None:
        voyageur.next = list2
    else:
        voyageur.next = list1

    return result_list.next
    
