class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1 #to not consider duplicates
            right = len(nums)-1
            while left < right:
                added = nums[i] + nums[left] + nums[right]

                if added < 0:
                    left+=1
                elif added > 0:
                    right -=1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    while left < right and nums[left] == triplet[1]:
                        left+=1
                    while left < right and nums[right] == triplet[2]:
                        right-=1
        return result
