

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_processed_str(s: str) -> str:
            len_s = len(s)
            ans = []
            fast_idx, slow_idx = 0, len_s - 1
            while fast_idx < len_s:
                if s[fast_idx] == '#':
                    if ans:
                        ans.pop()
                else:
                    ans.append(s[fast_idx])
                fast_idx += 1
            return str(ans)
        return get_processed_str(s) == get_processed_str(t)


s = "ab##"
t = "c#d#"
ss = Solution()
print(ss.backspaceCompare(s, t))