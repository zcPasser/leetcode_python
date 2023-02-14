class Solution:
    def get_string(self, s: str):
        stack = []
        for ch in s:
            if ch == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     return self.get_string(s) == self.get_string(t)

    def backspaceCompare(self, s: str, t: str) -> bool:
        idx_s, idx_t = len(s) - 1, len(t) - 1
        backspace_s, backspace_t = 0, 0
        while True:
            while idx_s > -1:
                if s[idx_s] == '#':
                    backspace_s += 1
                else:
                    if backspace_s > 0:
                        backspace_s -= 1
                    else:
                        break
                idx_s -= 1

            while idx_t > -1:
                if t[idx_t] == '#':
                    backspace_t += 1
                else:
                    if backspace_t > 0:
                        backspace_t -= 1
                    else:
                        break
                idx_t -= 1
            if idx_s < 0 or idx_t < 0:
                break
            if s[idx_s] != t[idx_t]:
                return False
            idx_s -= 1
            idx_t -= 1
        return idx_s == -1 and idx_t == -1


s = "nzp#o#g"
t = "b#nzp#o#g"
ss = Solution()
print(ss.backspaceCompare(s, t))