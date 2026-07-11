
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        maxheap = [] #has the frequencies of tasks
        count = collections.Counter(tasks)
        q = deque() #has remaining freq and time till next availibity
                    #[-cnt, idleTime]

        time = 0

        for i in count.values():
            heapq.heappush(maxheap, -i) #-i cause python only has minheap
        heapq.heapify(maxheap)
        
        while maxheap or q:
            time += 1
            if maxheap:
                f = 1 + heapq.heappop(maxheap) #we have processsed it so remaining time -1
                if f: # if it is not 0, theres still time left for this task
                    q.append([f, time + n])
        
            if q and time == q[0][1]:
                    heapq.heappush(maxheap, q.popleft()[0])
            
        return time
        
