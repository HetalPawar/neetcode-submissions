class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]
        
        # Convert into a max-heap by inverting values  
        max_heap = [-n for n in stones]  
        heapq.heapify(max_heap)  

        while len(max_heap)>1:

            # Access largest element (invert sign again)  
            #print("Largest element:", -max_heap[0])
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x != y:
                diff = abs(abs(x)-abs(y))
                heapq.heappush(max_heap, -diff)

        if len(max_heap) > 0:
            return -max_heap[0]
        else:
            return 0
