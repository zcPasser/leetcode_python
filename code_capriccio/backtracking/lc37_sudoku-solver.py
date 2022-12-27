class Solution:
    def __init__(self):
        self.vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def is_legal(self, board: list[list[str]], row: int, col: int, val: str) -> bool:
        for i in range(9):
            if board[row][i] == val or board[i][col] == val:
                return False
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == val:
                    return False
        return True

    def backtracking(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for idx in range(9):
                        if self.is_legal(board, i, j, self.vals[idx]):
                            board[i][j] = self.vals[idx]
                            if self.backtracking(board):
                                return True
                            board[i][j] = '.'
                    return False

        return True

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(board)
print(board)