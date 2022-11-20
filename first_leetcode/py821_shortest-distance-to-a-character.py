"""
description:
    1、Given a string s and a character c that occurs in s.、
    2、The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

return:
    an array of integers answer where answer.length == s.length
        and answer[i] is the distance from index i to the closest occurrence of character c in s.


"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        ans, last = [float('inf')] * len(s), None
        for i, ch in enumerate(s):
            if ch == c:
                if last is not None:
                    for j in range(i, (i - 1 + last) // 2, -1):
                        ans[j] = min(ans[j], i - j)
                else:
                    for j in range(i, -1, -1):
                        ans[j] = i - j
                last = i
            elif last is not None:
                ans[i] = min(ans[i], i - last)
        return ans
        # ans = []
        # idxs_of_c = [sys.maxsize]
        # for idx, ch in enumerate(s):
        #     if ch == c:
        #         idxs_of_c.append(idx)
        # idxs_of_c.append(sys.maxsize)
        # i = 1
        # for idx, ch in enumerate(s):
        #     if idx > idxs_of_c[i]:
        #         i += 1
        #     left_dist, right_dist = abs(idx - idxs_of_c[i - 1]), abs(idx - idxs_of_c[i])
        #     if left_dist <= right_dist:
        #         ans.append(left_dist)
        #     else:
        #         ans.append(right_dist)
        #
        # return ans


s = "loveleetcode"
c = "e"
so = Solution()
print(so.shortestToChar(s, c))