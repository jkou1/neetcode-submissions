import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        


        # want to look at every item using for loop
        # if list of len k is not full, just add item
        # if it is full, check if item can replace largest elt in list
        # if no, continue
        # if yes, then we replace largest item, and re-sort list
        # but how to sort items in list most efficiently?
        resList = []

        for i in range(len(points)):
            curDist = (points[i][0]**2 + points[i][1]**2) ** 0.5
            heapq.heappush(resList, (curDist, points[i]))
        
        realRes = []

        for i in range(k):
            realRes.append(heapq.heappop(resList)[1])
                
        return realRes