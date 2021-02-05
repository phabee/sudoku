import numpy as np

def getCandidates(sudoku, rowId, colId):
    allowed = set(range(1, 10))
    allowed.difference_update(sudoku[:,colId])
    allowed.difference_update(sudoku[rowId,:])
    # determine quadrant items
    qRow = rowId // 3
    qCol = colId // 3
    quadSet = sudoku[3*qRow:3*qRow+3, 3*qCol:3*qCol+3]
    allowed.difference_update(quadSet.flatten())
    return allowed

def findNextEmptyCell(sudoku, rowId, colId):
    row = rowId
    col = colId
    for i in range(row,9):
        for j in range(col,9):
            if sudoku[i,j] == 0:
                return i, j
        col = 0
    return None, None

def isSolved(sudoku):
    return sudoku.flatten().sum() == 405

def solve(sudoku, rowId = 0, colId = 0):
    # first determine next empty cell starting from rowId / colId, if current cell is not empty (!=0)
    if sudoku[rowId, colId] != 0:
        # field already set, find next empty cell
        rowId, colId = findNextEmptyCell(sudoku, rowId, colId)
        if rowId == None or colId == None:
            return sudoku
    # determine potential candidates for given cell
    cands = getCandidates(sudoku, rowId, colId)
    # loop through all candidates and
    for cand in cands:
        sudoku[rowId, colId] = cand
        sudoku = solve(sudoku, rowId, colId)
        if isSolved(sudoku):
            return sudoku
    sudoku[rowId, colId] = 0
    return sudoku

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sudoku = np.array([[0,7,2,4,8,5,0,0,0],
              [4,0,8,2,0,0,0,0,0],
              [5,0,0,0,0,9,4,0,0],
              [0,0,5,0,0,1,0,0,8],
              [0,0,0,0,6,0,0,0,0],
              [1,0,0,5,0,0,9,0,0],
              [0,0,4,1,0,0,0,0,5],
              [0,0,0,0,0,4,3,0,7],
              [0,0,0,7,3,8,2,1,0]])

    result = solve(sudoku)
    print(result)
