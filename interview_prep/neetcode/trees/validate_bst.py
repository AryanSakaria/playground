# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, min_range, max_range):
        if root.val > min_range and root.val < max_range:
            if root.left is None and root.right is None:
                return True
            if root.right is None:
                return self.dfs(root.left, min_range, root.val)
            if root.left is None:
                return self.dfs(root.right, root.val, max_range)
            return self.dfs(root.left, min_range, root.val) and self.dfs(root.right, root.val, max_range)
            
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))
        
