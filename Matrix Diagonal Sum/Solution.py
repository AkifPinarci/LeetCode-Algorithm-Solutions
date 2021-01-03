mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
total = 0
for i in range(len(mat)):
    if i == len(mat)//2 and len(mat) % 2 == 1:
        pass
    else:
        total += mat[i][i]

outerIndex = 0
for i in range(len(mat) - 1, -1, -1):
    total += mat[outerIndex][i]
    outerIndex += 1


print(total)