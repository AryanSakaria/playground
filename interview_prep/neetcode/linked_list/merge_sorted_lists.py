# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, trav = None, None
        while not list1 is None and not list2 is None:
            if list1.val < list2.val:
                if head is None:
                    head = list1
                    list1 = list1.next
                    trav = head
                else:
                    trav.next = list1
                    list1 = list1.next
                    trav = trav.next
                    #do something
            else:
                if head is None:
                    head = list2
                    list2 = list2.next
                    trav = head
                else:
                    #do something
                    trav.next = list2
                    list2 = list2.next
                    trav = trav.next
        
        while not list1 is None:
            if head is None:
                return list1
            else:
                trav.next = list1
                list1 = list1.next
                trav = trav.next
        while not list2 is None:
            if head is None:
                return list2
            else:
                trav.next = list2
                list2 = list2.next
                trav = trav.next
        return head
            

        