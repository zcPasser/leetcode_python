from collections import Counter

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []
        len_candidates = len(candidates)
        used = [False] * len_candidates
        def backtracking(start_idx: int, cur_sum: int):
            if cur_sum == target:
                ans.append(path[:])
                return
            nonlocal len_candidates
            for i in range(start_idx, len_candidates):
                # used[i - 1] == true，说明同一树枝candidates[i - 1]
                # used[i - 1] == false，说明同一树层candidates[i - 1]
                # 要对同一树层使用过的元素进行跳过
                if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                    continue
                # 剪枝
                if (cur_sum + candidates[i]) > target:
                    return
                path.append(candidates[i])
                used[i] = True
                backtracking(i + 1, cur_sum + candidates[i])
                path.pop()
                used[i] = False
            return
        if len_candidates != 0:
            # 首先把给candidates排序，让其相同的元素都挨在一起。
            candidates.sort()
            backtracking(0, 0)
        return ans

can = [10,1,2,7,6,1,5]
t = 8
s = Solution()
print(s.combinationSum2(can, t))