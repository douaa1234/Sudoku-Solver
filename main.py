def Valid_Number(grid, row, column, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][column] == num:
            return False
        
    leftCornerRow = row - row % 3
    leftCornerCol = column - column % 3 

    for x in range(3):
        for y in range(3):
            if grid[leftCornerRow + x][leftCornerCol + y] == num:
                return False 
            
    return True

def sudoku_solver(grid, row, column):
    # Move to the next row if column index exceeds
    if column == 9:
        row += 1
        column = 0
    # If we have reached the end of the grid
    if row == 9:
        return True

    if grid[row][column] > 0:
        return sudoku_solver(grid, row, column + 1)
    
    for num in range(1, 10):
        if Valid_Number(grid, row, column, num):
            grid[row][column] = num

            if sudoku_solver(grid, row, column + 1):
                return True
            
            # Reset cell (backtrack)
            grid[row][column] = 0

    return False

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if sudoku_solver(grid, 0, 0):
    for i in range(9):
        print(" ".join(str(grid[i][j]) for j in range(9)))
else:
    print('No solution for this Sudoku')
