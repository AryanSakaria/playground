# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        len_level = 1
        ans = []
        while len(q):
            children = 0
            for i in range(len_level):
                child = q.popleft()
                if child.left:
                    q.append(child.left)
                    children += 1 
                if child.right:
                    q.append(child.right)
                    children += 1
                if i == len_level - 1:
                    ans.append(child.val)
            len_level = children
        return ans

        