class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.n = 0

    def is_legal(self, row: int, col: int):
        for i in range(row - 1, -1, -1):
            if self.path[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i > -1 and j > -1:
            if self.path[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i > -1 and j < self.n:
            if self.path[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtracking(self, row: int):
        if self.n == row:
            self.ans.append([''.join(line) for line in self.path])
            return
        for i in range(self.n):
            if self.is_legal(row, i):
                self.path[row][i] = 'Q'
                self.backtracking(row + 1)
                self.path[row][i] = '.'

    def solveNQueens(self, n: int) -> list[list[str]]:
        # self.ans.clear()
        # self.path.clear()
        self.n = n
        self.path = [['.'] * self.n for _ in range(self.n)]
        self.backtracking(0)
        return self.ans


n = 4
s = Solution()
print(s.solveNQueens(n))