# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.good_nodes = 0
    
    def dfs(self, root, max_so_far):
        if root is None:
            return
        if root.val >= max_so_far:
            self.good_nodes += 1
        self.dfs(root.left, max(max_so_far, root.val))
        self.dfs(root.right, max(max_so_far, root.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.good_nodes
        