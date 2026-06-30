# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 


        def helper(node, mintree, maxtree):
            if not node:
                return True 

            if not (mintree < node.val < maxtree):
                return False
            
            lefttree = helper(node.left, mintree, node.val)
            righttree = helper(node.right, node.val, maxtree)
            return lefttree and righttree

        isvalid = helper(root, float('-inf'), float('inf'))
        return isvalid 