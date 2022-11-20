from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_legal(cnt1: Counter, cnt2: Counter) -> bool:
            for k, v in cnt2.items():
                if cnt1[k] < v:
                    return False
            return True
        start_idx, end_idx = 0, 0
        len_s = len(s)
        cnt_t = Counter(t)
        cnt_s = Counter()

        len_ans = len_s + 1
        ans = ''
        # while s[start_idx] not in cnt_t:
        #     start_idx += 1
        while end_idx < len_s:
            cnt_s[s[end_idx]] += 1
            while is_legal(cnt_s, cnt_t):
                if (end_idx - start_idx + 1) < len_ans:
                    ans = s[start_idx: end_idx + 1]
                    len_ans = end_idx - start_idx + 1
                cnt_s[s[start_idx]] -= 1
                if cnt_s[s[start_idx]] == 0:
                    cnt_s.pop(s[start_idx])
                start_idx += 1
            end_idx += 1
        return ans


ss = "a"
tt = "a"
s = Solution()
print(s.minWindow(ss, tt))


