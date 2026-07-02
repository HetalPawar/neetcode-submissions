# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #if the tree is empty then return empty 
        if not root:
            return []

        #we will use level order traversal
        output = []
        q = collections.deque([root])

        while q:
            qlen = len(q)
            for i in range(qlen):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
                if i == (qlen - 1):
                    output.append(curr.val)
        
        return output