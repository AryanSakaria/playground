"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head_ = head
        copy_dict = {None:None}
        while head_:
            copy_dict[head_] = Node(head_.val)
            head_ = head_.next
        head_ = head
        while head_:
            copy_dict[head_].next = copy_dict[head_.next]
            copy_dict[head_].random = copy_dict[head_.random]
            head_ = head_.next

        return copy_dict[head]