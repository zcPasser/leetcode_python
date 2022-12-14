class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_to_alp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        path = []
        def backtracking(cur_idx, len_digits):
            if cur_idx == len_digits:
                ans.append(''.join(path))
                return
            for ch in num_to_alp[digits[cur_idx]]:
                path.append(ch)
                backtracking(cur_idx + 1, len_digits)
                path.pop()
            return
        len_digits = len(digits)
        if len_digits != 0:
            backtracking(0, len(digits))
        return ans

digits = "23"
s = Solution()
print(s.letterCombinations(digits))
