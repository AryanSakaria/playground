"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node):
        if node is None:
            return None
        if node in self.visited:
            return self.visited[node]
        
        new_copy = Node(node.val)
        self.visited[node] = new_copy
        for neighbor in node.neighbors:
            new_copy.neighbors.append(self.dfs(neighbor))
        return new_copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = {}
        return self.dfs(node)
        