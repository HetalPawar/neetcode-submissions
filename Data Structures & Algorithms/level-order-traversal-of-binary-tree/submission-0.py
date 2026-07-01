# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #deal with empty case
        if not root:
            return []
        output = []

        #now queue is to 
        q = collections.deque([])
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            output.append(level)
        return output