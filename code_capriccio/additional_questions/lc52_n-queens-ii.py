class Solution:
    def __init__(self):
        self.ans = 0
        self.chessboard = None

    def is_valid(self, row: int, col: int, n: int):
        for i in range(row):
            if self.chessboard[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i > -1 and j > -1:
            if self.chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i > -1 and j < n:
            if self.chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtracking(self, row: int, n: int):
        if row == n:
            self.ans += 1
            return
        for i in range(n):
            if self.is_valid(row, i, n):
                self.chessboard[row][i] = 'Q'
                self.backtracking(row + 1, n)
                self.chessboard[row][i] = '.'

    def totalNQueens(self, n: int) -> int:
        self.chessboard = [['.' for _ in range(n)] for _ in range(n)]
        self.backtracking(0, n)
        return self.ans

n = 4
s = Solution()
print(s.totalNQueens(n))
