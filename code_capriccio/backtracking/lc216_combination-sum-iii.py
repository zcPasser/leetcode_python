class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans =[]
        path = []
        def backtracking(start_idx: int, target: int, nums: int):
            if target == 0 and nums == 0:
                ans.append(path[:])
                return
            elif target == 0 or nums == 0:
                return

            for i in range(start_idx, 9 - nums + 2):
                if i > target:
                    return
                path.append(i)
                backtracking(i + 1, target - i, nums - 1)
                path.pop()
            return
        backtracking(1, n, k)
        return ans

k = 3
n = 7
s = Solution()
print(s.combinationSum3(k, n))


