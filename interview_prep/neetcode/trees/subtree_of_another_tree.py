# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and not q is None:
            return False
        if q is None and not p is None:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and not subRoot is None:
            return False
        if subRoot is None and not root is None:
            return False
        if subRoot is None and root is None:
            return True
        same_tree = False
        if root.val == subRoot.val:
            same_tree = self.isSameTree(root,subRoot)
            
        return same_tree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        