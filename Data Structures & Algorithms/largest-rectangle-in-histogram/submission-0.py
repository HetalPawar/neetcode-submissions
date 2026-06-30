class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index))
                start = index
            stack.append((start,h))
        
        for i,h in stack: #these go to end of list or widht is len(list) - 1
            maxarea = max(maxarea, h*((len(heights)-i)))
        return maxarea