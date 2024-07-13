# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.arr = []
    
    def dfs_serial(self, root):
        if root is None:
            self.arr.append("N")
            return
        self.arr.append(str(root.val))
        self.dfs_serial(root.right)
        self.dfs_serial(root.left)



    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.arr = []
        self.dfs_serial(root)
        return ",".join(self.arr)
        
    def de_dfs(self):
        if self.res[self.i] == "N":
            self.i += 1
            return None

        root = TreeNode(int(self.res[self.i]))
        self.i += 1
        root.right = self.de_dfs()
        root.left = self.de_dfs()
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.res = data.split(",")
        self.i = 0
        root = self.de_dfs()
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))