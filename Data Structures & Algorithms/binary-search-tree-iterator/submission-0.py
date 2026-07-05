# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        while root is not None:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return bool(self.stack)

    def next(self) -> int:
        temp = self.stack.pop()
        node = temp.right
        while node is not None:
            self.stack.append(node)
            node = node.left
        return temp.val    
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()