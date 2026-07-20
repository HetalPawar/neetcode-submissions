import random
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(nopen, nclose):
            #found valid
            if nopen == nclose == n:
                res.append(''.join(stack))
                return
            #add open only if o < n
            if nopen < n: 
                stack.append('(')
                backtrack(nopen + 1, nclose)
                stack.pop()

            #add close only if c < o
            if nclose < nopen:
                stack.append(')')
                backtrack(nopen, nclose + 1)
                stack.pop()
        backtrack(0, 0 )
        return res

    '''\BRUTE FORCE
    def isvalidparethesis(self, candidate):
        closed = { ')' : '(', ']': '[', '}':"{"}
        stack = []
        for c in candidate:
            if c in closed:
                if stack and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        if n == 0:
            return []
        res = [] 
        bracket = ['(', ')']   

        def backtrack(path):
            #base case
            if len(path) == n*2 and self.isvalidparethesis(path):
                res.append("".join(path))
                return

            for i in bracket:
                
                #UPDATE
                path.append(i)
                backtrack(path)
                path.pop()

        backtrack([])
        return res'''