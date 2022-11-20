
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        m = len(moves)
        # 用数组记录0 - 2行、0 - 2列、正对角线、副对角线是否已满3个棋子
        # count[0 - 2] 对应0 - 2行、count[3 - 5] 对应0 - 2 列、count[6] 对应正对角线、count[7]对应副对角线
        count = [0] * 8
        # 思路第2步已解释为何只需考虑最后一个落棋的人
        # 倒序统计此人走棋情况
        for i in range(m - 1, -1, -2):
            # 此棋对行的影响
            count[moves[i][0]] += 1
            # 此棋对列的影响
            count[moves[i][1] + 3] += 1
            # 此棋对正对角线的影响
            if moves[i][0] == moves[i][1]:
                count[6] += 1
            # 此棋对副对角线的影响 (
            # 此处为3x3的情况，其余大小的棋盘可以类推
            if moves[i][0] + moves[i][1] == 2:
                count[7] += 1
            # 满3个棋子则胜利
            if count[moves[i][0]] == 3 or count[moves[i][1] + 3] == 3 or count[6] == 3 or count[7] == 3:
                # A先B后 则总长度为偶时 最后为B 反之为A
                return "B" if m % 2 == 0 else "A"

        # 未胜时，棋盘未下满则继续
        if len(moves) < 9:
            return "Pending"

        # 未胜时，棋盘下满则平局结束
        return "Draw"

        # if len(moves) < 5:
        #     return 'Pending'
        # cnt_empty = 9
        # signs = [1, 0]
        # girds = [-1] * cnt_empty
        #
        # def is_winner(r: int, c: int, sign: int) -> bool:
        #     # judge the row
        #     idx_start = r * 3
        #     if girds[idx_start] == girds[idx_start + 1] == girds[idx_start + 2] == sign:
        #         return True
        #     # judge the column
        #     idx_start = c
        #     if girds[idx_start] == girds[idx_start + 3] == girds[idx_start + 6] == sign:
        #         return True
        #     # judge the diagonal line
        #     idx = r * 3 + c
        #     if (r == c and girds[0] == girds[4] == girds[8] == sign) or \
        #             (idx in (2, 4, 6)and girds[2] == girds[4] == girds[6] == sign):
        #         return True
        #     return False
        #
        # for [r, c] in moves:
        #     cnt_empty -= 1
        #     if cnt_empty == -1:
        #         return 'Draw'
        #     idx = cnt_empty % 2
        #     girds[r * 3 + c] = signs[idx]
        #     if cnt_empty <= 4 and is_winner(r, c, signs[idx]):
        #         return 'A' if idx == 0 else 'B'
        #
        # return 'Pending' if cnt_empty != 0 else 'Draw'


moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
s = Solution()
print(s.tictactoe(moves))

