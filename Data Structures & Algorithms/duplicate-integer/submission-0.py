class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #loop through it twice to get any dupllicates
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True 
        else:
            return False
        #use functions - like find
        #hashmap
        