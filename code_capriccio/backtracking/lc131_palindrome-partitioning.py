class Solution:
    def __init__(self):
        self.ans = []
        self.path = []

    def is_palindrome(self, s, start: int, end: int) -> bool:
        i, j = start, end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def backtracking(self, s: str, start_idx: int):
        if start_idx >= len(s):
            self.ans.append(self.path[:])
            return

        for i in range(start_idx, len(s)):
            if self.is_palindrome(s, start_idx, i):
                self.path.append(s[start_idx: i + 1])
                self.backtracking(s, i + 1)
                self.path.pop()
            else:
                continue

    def partition(self, s: str) -> list[list[str]]:
        if len(s) != 0:
            self.backtracking(s, 0)
        return self.ans


ss = "aab"
s = Solution()
print(s.partition(ss))