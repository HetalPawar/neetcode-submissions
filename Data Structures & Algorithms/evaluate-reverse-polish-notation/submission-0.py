class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for curr in tokens:
            if curr == '+':
                stack.append( stack.pop() + stack.pop())
            elif curr == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif curr == '*':
                stack.append(stack.pop() * stack.pop())
            elif curr == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(curr))
        return stack.pop()
