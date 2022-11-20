from collections import Counter


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        cnt_in_degree = Counter(b for _, b in trust)
        cnt_out_degree = Counter(a for a, _ in trust)
        return next((i for i in range(1, n + 1) if cnt_in_degree[i] == n - 1 and cnt_out_degree[i] == 0), -1)
        # if n == 1 and not trust:
        #     return 1
        # trust_people = {}
        # trusted_people = set()
        # for a, b in trust:
        #     if a not in trust_people:
        #         trust_people[a] = []
        #     trust_people[a].append(b)
        #     if b not in trusted_people:
        #         trusted_people.add(b)
        #
        # if len(trust_people) == n or len(trust_people) < n - 1:
        #     return -1
        # if len(trusted_people) == 1:
        #     return trust[0][1]
        #
        # for b in trusted_people:
        #     if b not in trust_people:
        #         flag = True
        #         for k, v in trust_people.items():
        #             if b not in v:
        #                 flag = False
        #                 break
        #         if flag:
        #             return b
        #
        # return -1


n = 4
trust = [[1,3],[1,4],[2,3]]
s = Solution()
print(s.findJudge(n, trust))