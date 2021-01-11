class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        if (coordinates[1][1] - coordinates[0][1]) != 0:
            slope = (coordinates[1][0] - coordinates[0][0])/(coordinates[1][1] - coordinates[0][1])
            for i in range(1,len(coordinates)):
                if (coordinates[i][1] - coordinates[i-1][1]) == 0:
                    return False
                if (coordinates[i][0] - coordinates[i-1][0])/(coordinates[i][1] - coordinates[i-1][1]) != slope:
                    return False
        else:
            for i in range(len(coordinates) - 1):
                if coordinates[i][1] != coordinates[i+1][1]:
                    return False
        return True
