# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None

    def dfs_helper(self, root):
        if root is None:
            return 0
        root_val = root.val
        left_val = self.dfs_helper(root.left)
        right_val = self.dfs_helper(root.right)
        upstream_val = root_val + max(left_val, right_val)
        if self.ans == None:
            self.ans = left_val + root_val + right_val
        else:
            self.ans = max(self.ans, 
                    root_val, 
                    root_val + left_val, 
                    root_val + right_val, 
                    root_val + left_val + right_val)
        return max(upstream_val, root_val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs_helper(root)
        return self.ans
        