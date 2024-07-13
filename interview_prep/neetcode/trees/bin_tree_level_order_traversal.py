# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        len_level = 1
        ans = []
        while len(q):
            total_children = 0
            level_arr = []
            for i in range(len_level):
                cur_child = q.popleft()
                level_arr.append(cur_child.val)
                if cur_child.left:
                    q.append(cur_child.left)
                    total_children += 1
                if cur_child.right:
                    q.append(cur_child.right)
                    total_children += 1
            ans.append(level_arr)
            len_level = total_children

        return ans
        