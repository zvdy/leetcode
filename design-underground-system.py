from typing import *
class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.timeMap = {}
        self.countMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, checkInTime = self.checkInMap[id]
        key = station + '_' + stationName
        if key not in self.timeMap:
            self.timeMap[key] = 0
            self.countMap[key] = 0
        self.timeMap[key] += t - checkInTime
        self.countMap[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + '_' + endStation
        return self.timeMap[key] / self.countMap[key]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)