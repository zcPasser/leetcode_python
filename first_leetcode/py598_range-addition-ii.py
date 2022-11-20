"""
1、m x n 的矩阵 M ，初始化时所有的 0；一个操作数组 op ，其中 ops[i] = [ai, bi]。
2、对于当前[ai, bi]，当所有的(x, y)满足 0 <= x < ai 和 0 <= y < bi 时， M[x][y] 应该加 1。

返回：
    矩阵中最大整数的个数 。
"""


class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if len(ops) == 0:
            return m * n

        return min((op[0] for op in ops)) * min((op[1] for op in ops))

        # mina, minb = m, n
        # for a, b in ops:
        #     mina = min(mina, a)
        #     minb = min(minb, b)
        # return mina * minb




s = Solution()
m, n = 26, 17
ops = [[20,10],[26,11],[2,11],[4,16],[2,3],[23,13],[7,15],[11,11],[25,13],[11,13],[13,11],[13,16],[26,17]]
print(s.maxCount(m, n, ops))