# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxpath = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper_dfs(node):
            if not node:
                return 0

            #we are doing postfix : left -> right -> root

            #caluclate the left and right side tree 
            #if its negative, ignore it by assigning 0

            leftside_sum = max(0, helper_dfs(node.left))
            rightside_sum = max(0, helper_dfs(node.right))

            #if the currpath is the V
            currpath = node.val + leftside_sum + rightside_sum

            self.maxpath = max(currpath, self.maxpath)

            #return the longest path to the parent
            return node.val + max(leftside_sum, rightside_sum)
    
        helper_dfs(root)
        return self.maxpath



        