class Solution:
    def __init__(self):
        self.ans = []
        self.path = []

    def is_legal(self, s: str, start_idx: int, end_idx: int) -> bool:
        if start_idx > end_idx:
            return False
        if s[start_idx] == '0' and start_idx != end_idx:
            return False
        val = 0
        for i in range(start_idx, end_idx + 1):
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                return False
            val = val * 10 + (ord(s[i]) - ord('0'))
            if val > 255:
                return False
        return True

    def backtracking(self, s: str, start_idx: int, point_nums: int):
        if point_nums == 3:
            if self.is_legal(s, start_idx, len(s) - 1):
                self.path.append(s[start_idx:])
                self.ans.append('.'.join(self.path))
                self.path.pop()
            return
        for i in range(start_idx, len(s)):
            if self.is_legal(s, start_idx, i):
                self.path.append(s[start_idx: i + 1])
                self.backtracking(s, i + 1, point_nums + 1)
                self.path.pop()
            else:
                break

    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) > 0:
            self.backtracking(s, 0, 0)
        return self.ans

s = "25525511135"
ss = Solution()
print(ss.restoreIpAddresses(s))