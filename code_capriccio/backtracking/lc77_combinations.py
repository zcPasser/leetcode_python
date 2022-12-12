class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        path = []
        def backtracking(start_idx: int):
            if len(path) == k:
                ans.append(path[:])
                return
            # 剪枝操作：保证 剩余元素 足够选出 满足k个的组合
            for i in range(start_idx, n - (k - len(path)) + 2):
            # for i in range(start_idx, n + 1):
                path.append(i)
                backtracking(i + 1)
                path.pop()

        backtracking(1)
        return ans