

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        idx_i, idx_j = 0, 0
        m, n = len(board), len(board[0])
        is_done = False
        for i in range(m):
            if is_done:
                break
            for j in range(n):
                if board[i][j] == 'R':
                    idx_i, idx_j = i, j
                    is_done = True
                    break
        ans = 0

        step = [1] * 4

        while idx_i - step[0] >= 0:
            if board[idx_i - step[0]][idx_j] == 'p':
                ans += 1
                break
            elif board[idx_i - step[0]][idx_j] == 'B':
                break
            else:
                step[0] += 1

        while idx_i + step[1] < m:
            if board[idx_i + step[1]][idx_j] == 'p':
                ans += 1
                break
            elif board[idx_i + step[1]][idx_j] == 'B':
                break
            else:
                step[1] += 1

        while idx_j - step[2] >= 0:
            if board[idx_i][idx_j - step[2]] == 'p':
                ans += 1
                break
            elif board[idx_i][idx_j - step[2]] == 'B':
                break
            else:
                step[2] += 1

        while idx_j + step[3] < n:
            if board[idx_i][idx_j + step[3]] == 'p':
                ans += 1
                break
            elif board[idx_i][idx_j + step[3]] == 'B':
                break
            else:
                step[3] += 1

        return ans


board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

s = Solution()
print(s.numRookCaptures(board))

