class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []
        def backtracking(start_idx: int, cur_sum: int):
            if cur_sum == target:
                ans.append(path[:])
                return

            nonlocal len_candidates
            for i in range(start_idx, len_candidates):
                if (cur_sum + candidates[i]) > target:
                    return
                path.append(candidates[i])
                backtracking(i, cur_sum + candidates[i])
                path.pop()
            return
        len_candidates = len(candidates)
        if len_candidates != 0:
            candidates.sort()
            backtracking(0, 0)
        return ans

candidates = [2,3,6,7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))
