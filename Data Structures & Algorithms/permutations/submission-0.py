class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack( path):
            #base case
            if len(path) == len(nums):
                res.append(list(path))
                return

            for i in range(len(nums)):
                #include this element. constraints
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()

        
        backtrack([])
        return res