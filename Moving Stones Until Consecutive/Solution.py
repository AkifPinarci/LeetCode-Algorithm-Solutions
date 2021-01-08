class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        arr = sorted([a, b, c])
        maxmove = (arr[1] - arr[0]) + (arr[2] - arr[1]) - 2
        minmove = int
        if (arr[1] - arr[0] == 2) or (arr[2] - arr[1]) == 2:
            minmove = 1
        elif (arr[1] - arr[0] > 1) and (arr[2] - arr[1]) > 1:
            minmove = 2
        else:
            minmove = 1
        if maxmove == 0:
            return [0,0]
        else:
            return [minmove, maxmove]