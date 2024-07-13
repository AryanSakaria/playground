# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_balanced = True
    def depth(self, root):
        if root is None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if abs(left_depth - right_depth) > 1:
            self.is_balanced = False
        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.depth(root)
        return self.is_balanced
        