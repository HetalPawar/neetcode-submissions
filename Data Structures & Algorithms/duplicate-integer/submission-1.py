class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if len(nums) > len(new):
            return True
        else:
            return False