class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
             
            if nums[left] <= nums[right]:
                minimum = min(minimum, nums[left])
                break

            middle = (right+left)//2
            minimum = min(minimum, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return minimum