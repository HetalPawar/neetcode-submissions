class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            #base case
            if index == len(nums):
                res.append(list(path))
                return

            #include this element
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            #dont include this element
            backtrack(index+1, path)
        
        backtrack(0, [])
        return res
        