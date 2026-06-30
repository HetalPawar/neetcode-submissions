class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] #(temperature, index)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                days = i - index #i is more than index
                ans[index] = days
            stack.append((temperatures[i], i))
        return ans
