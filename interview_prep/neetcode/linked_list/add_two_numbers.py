# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1_, l2_ = l1, l2
        head = None
        while l1_ or l2_:
            sum = 0
            if l1_:
                sum += l1_.val
                l1_ = l1_.next
            if l2_:
                sum += l2_.val
                l2_ = l2_.next
            sum += carry
            carry = sum //10
            if head == None:
                head = ListNode(sum%10)
                trav = head
            else:
                trav.next = ListNode(sum%10)
                trav = trav.next
        if carry:
            trav.next = ListNode(carry)
        return head