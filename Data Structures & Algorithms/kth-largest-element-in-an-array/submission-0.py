class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if len(nums) <1:
            return None
        
        minheap = nums
        heapq.heapify(minheap)

        maxi = heapq.nlargest(k, minheap)

        return maxi[-1]