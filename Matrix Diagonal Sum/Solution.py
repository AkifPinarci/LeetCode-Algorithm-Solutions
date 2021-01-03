class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        
        if len(mat) == 1:
            return mat[0][0]
        
        elif len(mat) == 0:
            return 0
        
        for i in range(len(mat)):
            if i == len(mat)//2 and len(mat) % 2 == 1:
                pass
            else:
                total += mat[i][i]

        outerIndex = 0
        for i in range(len(mat) - 1, -1, -1):
            total += mat[outerIndex][i]
            outerIndex += 1
            
        return total