
def SudokuSolver(grid: list):
    empty_cell = findEmptyCell(grid)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for number in range(1, 10):
        if isValid(grid, number, col, row):
            grid[row][col] = number
            if SudokuSolver(grid):
                return True
            
            grid[row][col] = 0
    return False

def findEmptyCell(grid: list):
    for row in range(0, 9):
        for collumn in range(0, 9):
            if grid[row][collumn] == 0:
                return row, collumn
    
    return None

def isValid(grid: list, number: int, col: int, line: int):
    
    for collumn in range(0, 9):
        if grid[line][collumn] == number:
            return False
    
    for row in range(0, 9):
        if grid[row][col] == number:
            return False
    
    startRow = (line // 3) * 3
    startCollumn = (col // 3) * 3
    
    for rowSub in range(startRow, startRow + 3):
        for colSub in range(startCollumn, startCollumn + 3):
            if grid[rowSub][colSub] == number:
                return False
            
    return True