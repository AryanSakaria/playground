# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def dfs(self, root, p, q):
        if root is None:
            return
        if p.val < root.val and q.val < root.val:
            self.dfs(root.left, p, q)
            return
        if p.val > root.val and q.val > root.val:
            self.dfs(root.right, p, q)
            return
        else:
            self.ans = root 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans
        