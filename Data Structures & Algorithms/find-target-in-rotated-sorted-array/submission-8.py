class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            
            middle = (right+left)//2
            if nums[middle] == target:
                return middle

            #left portion
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            #right sorted portion     
            elif nums[middle] <= nums[left]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            
        return -1
        
        