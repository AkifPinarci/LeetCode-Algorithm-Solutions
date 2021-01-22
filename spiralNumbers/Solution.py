# CodeSignal
def spiralNumbers(n):
    rows, cols = (n,n) 
    result = [[0 for i in range(cols)] for j in range(rows)] 

    track = 1
    top = 0
    right = n-1
    bottom = n-1
    left = 0
    unique = 0

    while track != n * n + 1:
        for i in range(top, right+1):

            result[top][i] = track
            track += 1
        top += 1

        for j in range(top, right):
            result[j][right] = track
            track += 1
        right -= 1

        for i in range(bottom, left, -1):
            result[bottom][i] = track
            track += 1
        bottom -= 1
        
        for i in range(n - left-1, top-1, -1):
            result[i][left] = track
            track += 1
        left += 1
    return result
            
