import heapq
class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []

        for i in arr:
            diff = abs(i-x)
            heapq.heappush(maxheap, (-diff,-i))

            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        out = []
        while maxheap:
            v = heapq.heappop(maxheap)
            out.append(-v[1])

        return sorted(out)