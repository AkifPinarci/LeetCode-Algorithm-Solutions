def sudoku(grid):
    check = set()
    check2 = set()
    check3= set()
    for i in grid:
        check.add(tuple(sorted(i)))
    if len(check) != 1:
        return False
    for i in range(len(grid)):
        liste = []
        for j in range(len(grid[i])):
            liste.append(grid[j][i])
        check2.add(tuple(sorted(liste)))
    if len(check2) != 1:
        return False
    for i in range(0, 9, 3):
        liste2 = []
        for j in range(0, 9, 3):
            liste2 = (grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
            print(liste2)
            check3.add(tuple(sorted(liste2)))
    if len(check3) != 1:
        return False
    
    for i in grid:
        if len(set(i)) != 9:
            return False
    return True