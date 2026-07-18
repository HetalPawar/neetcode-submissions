class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(index, path):
            #base case
            if index == len(nums):
                res.append(list(path))
                return
            if index+1 > len(nums):
                return
            
            #include this path
            path.append(nums[index])
            backtrack(index +1 , path)
            path.pop()

            #dont include this path
            while index+1 < len(nums) and nums[index] == nums[index + 1]:
                index+=1
            backtrack(index + 1, path)


        backtrack(0,[])
        return res
