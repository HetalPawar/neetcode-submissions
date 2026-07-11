class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()  # sorts by num
        left, right = 0, len(nums)-1
        while left < right:
            if arr[left][0] + arr[right][0] == target:
                i, j = arr[left][1], arr[right][1]
                return [min(i, j), max(i, j)]
            elif arr[left][0] + arr[right][0] > target:
                right -= 1
            else:
                left += 1
