class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, path, currsum):
            #base case
            if currsum == target:
                res.append(list(path))
                return

            for i in range(index, len(nums)):
                if currsum > target:
                    currsum = 0
                    return

                path.append(nums[i])
                backtrack(i, path, currsum + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return res