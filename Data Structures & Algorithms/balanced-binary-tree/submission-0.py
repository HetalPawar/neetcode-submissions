# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper_dfs(node):
            if not node:
                return [True, 0] # empty tree has height 0 and is balenced
            
            left = helper_dfs(node.left)
            right = helper_dfs(node.right)
            #are elft and right balenced?
            LR = left[0] and right[0]
            #actual balence condition that height diff swhoud not be more than 1
            balenced = LR and (abs(left[1] - right[1]) <= 1) #we use abs as either can be bigger
            #max height? left or right, whcihever is greater is the height of that subtree
            maxH = 1 + max(left[1], right[1]) #+1 cause we need to coutn the curr node also
            
            return [balenced, maxH]

        isbalenced = helper_dfs(root)
        return isbalenced[0]