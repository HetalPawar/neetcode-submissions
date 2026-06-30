"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out = []

        def dfs_helper(node):
            if node is None:
                return None
            
            for i in node.children:
                dfs_helper(i)
            
            out.append(node.val)
        
        dfs_helper(root)
        return out
