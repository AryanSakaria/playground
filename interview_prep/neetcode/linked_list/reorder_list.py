# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, next = None, None
        while not head is None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        trav, n = head, 0
        while trav:
            n+=1
            trav = trav.next
        if n < 3:
            return head

        trav = head
        half = n//2
        while half -1:
            trav = trav.next
            half -= 1
        trav_next = trav.next
        trav.next = None
        trav = trav_next
        
        trav = self.reverseList(trav)
        head_, trav_ = head, trav
        half = n//2
        while half:
            head_next, trav_next = head_.next, trav_.next
            head_.next = trav_
            if head_next:
                trav_.next = head_next
                head_ = head_next
                trav_ = trav_next
            half -= 1
        
