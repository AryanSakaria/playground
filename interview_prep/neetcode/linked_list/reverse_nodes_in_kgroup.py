# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        new_tail, trav = head, head
        prev = None

        while k:
            trav_next = trav.next
            trav.next = prev
            
            prev = trav
            trav = trav_next
            k -= 1

        return prev, new_tail, trav


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, count_ptr = 0, head
        while count_ptr:
            count_ptr = count_ptr.next
            count += 1
        
        dummyNode = ListNode()
        prev_tail = dummyNode
        travel_ptr = head

        for i in range(count//k):
            new_head, new_tail, next_travel = self.reverse(travel_ptr, k)
            prev_tail.next = new_head
            new_tail.next = next_travel

            prev_tail = new_tail
            travel_ptr = next_travel

        return dummyNode.next