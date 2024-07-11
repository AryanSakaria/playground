# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        head_ = head
        count = 0
        while head_:
            count += 1
            head_ = head_.next
        print(count)
        reach = count - n
        head_ = head
        prev = head_
        while reach:
            reach -= 1
            print("head val", head_.val)
            prev = head_
            head_ = head_.next
        
        prev.next = head_.next
        if head_ == head:
            head = head.next
        return head
     