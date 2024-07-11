# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from queue import PriorityQueue
        q = PriorityQueue()
        count = 0
        for i in range(len(lists)):
            head_i = lists[i]
            if head_i:
                q.put((head_i.val, count, head_i))
                count += 1
        dummyNode = ListNode()
        trav = dummyNode
        while not q.empty():
            _, _, list_i = q.get()
            trav.next = list_i
            trav = list_i
            if list_i.next:
                list_i_next = list_i.next
                q.put((list_i_next.val, count, list_i_next))
                count += 1
        return dummyNode.next