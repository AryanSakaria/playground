# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preorder, inorder, l_p, r_p, l_i, r_i):
        
        if l_p > r_p or l_i > r_i:
            return None
        root_node = TreeNode(preorder[l_p])
        for i in range(l_i, r_i + 1):
            if inorder[i] == preorder[l_p]:
                break
        len_left_tree = i - l_i
        len_right_tree = r_i - i

        root_node.left = self.helper(preorder, inorder, l_p + 1, l_p + len_left_tree, l_i, i - 1)
        root_node.right = self.helper(preorder, inorder, l_p + len_left_tree + 1, r_p, i + 1, r_i)
        return root_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, inorder, 0, len(preorder)-1, 0, len(preorder)-1)
