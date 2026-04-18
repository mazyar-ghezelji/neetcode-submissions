# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        current = ListNode()
        if list1 and list2:
            if list1.val <= list2.val:# set the head
                head = list1
                current = list1
                list1 = list1.next
            else :
                head = list2
                current = list2
                list2 = list2.next
        elif list1 and not list2:
            head = list1
            current = list1
            list1 = list1.next
        elif list2 and not list1:
            head = list2
            current = list2
            list2 = list2.next
        else:
            return list1
        while list1!= None or list2!=None:

            if list1 == None:
                current.next = list2
                current = current.next
                list2 = list2.next

            elif list2 == None:
                current.next = list1
                current = current.next
                list1 = list1.next
            elif list1.val <= list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        return head

        