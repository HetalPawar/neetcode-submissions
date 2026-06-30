class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        prod = 1
        for i in range(len(nums)):
            prefix[i] = int(prod)
            prod *= nums[i]
        prod= 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = int(prod)
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums)):
            prod = suffix[i]*prefix[i]
            output.append(int(prod))

        return output