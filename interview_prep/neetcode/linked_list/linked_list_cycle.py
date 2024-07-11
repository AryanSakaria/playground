# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit, hare = head, head
        while True:
            if hare is None:
                return False
            if rabbit is None:
                return False
            if rabbit.next is None:
                return False
            hare = hare.next
            rabbit = rabbit.next.next
            if hare == rabbit:
                return True
        