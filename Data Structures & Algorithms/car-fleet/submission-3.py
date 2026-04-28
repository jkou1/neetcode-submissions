class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleets = 0

        # if car is further from target but takes less time,
        # same fleet
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append((position[i], speed[i]))
        
        posSpeed.sort(reverse = True)

        fleetTime = float('-inf')
        for i in range(len(position)):
            curTime = (target - posSpeed[i][0]) / posSpeed[i][1]
            if curTime > fleetTime:
                fleetTime = curTime
                numFleets += 1
        return numFleets
        
        

