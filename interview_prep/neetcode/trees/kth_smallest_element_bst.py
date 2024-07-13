# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.k = 0
    def dfs(self, root):
        if not self.k:
            return
        if root.left is None and root.right is None:
            if self.k:
                self.k -= 1
                self.ans = root.val
            return 
        if not self.k:
            return
        if not root.left is None and self.k: self.dfs(root.left)
        if self.k:
            self.k -= 1
            self.ans = root.val
        else:
            return
        if not root.right is None and self.k: self.dfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.dfs(root)
        return self.ans

        