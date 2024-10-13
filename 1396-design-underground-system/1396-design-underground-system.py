class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.totMap = {} # (start, end )-> 
        

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        start, time = self.checkInMap[id]
        route = (start, endStation)
        if route not in self.totMap:
            self.totMap[route] = [0,0]
        self.totMap[route][0] += t - time
        self.totMap[route][1] += 1        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totMap[(startStation, endStation)]
        return total / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)