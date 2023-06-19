class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope=self.getSlope(coordinates[1],coordinates[0])
        for i in range(2, len(coordinates)):
            m=self.getSlope(coordinates[i],coordinates[0])
            if slope!=m:
                return False
        return True

    def getSlope(self, p2: list[int], p1: list[int]):
        if p2[0]==p1[0]:
            return 500000
        return ((p2[1]-p1[1])/(p2[0]-p1[0]))