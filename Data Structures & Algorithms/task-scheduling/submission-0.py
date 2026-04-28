class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()

        # now we want to iterate thru all items in maxHeap or
        # in the queue

        curTime = 0
        while maxHeap or q:
            # pop the max count, store it's decremented value in the q,
            # along with the cur time plus the waiting delay
            if maxHeap:
                curCount = 1 + heapq.heappop(maxHeap)
                if curCount < 0:
                    q.append([curCount, curTime + n])

            if q and q[0][1] <= curTime:
                heapq.heappush(maxHeap, q.popleft()[0])

            curTime += 1

        return curTime

