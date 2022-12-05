from collections import Counter

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        cnt = [set() for _ in range(n + 1)]
        for road in roads:
            a, b = road[0], road[1]
            cnt[a].add(b)
            cnt[b].add(a)
        roads.sort(key=lambda x: x[2])

        ans = roads[0][2]

        def exist_path(p1: int, p2: int) -> bool:
            if p2 in cnt[p1] or p2 == p1:
                return True
            for p in cnt[p1]:
                if not visited[p]:
                    visited[p] = True
                    if exist_path(p, p2):
                        return True
            return False

        for road in roads:
            a, b, dist = road[0], road[1], road[2]
            visited = [False] * (n + 1)
            to_1 = (exist_path(a, 1) or exist_path(b, 1))
            visited = [False] * (n + 1)
            to_n = (exist_path(a, n) or exist_path(b, n))
            if to_1 and to_n:
                return dist
        return ans


n = 13
nums = [[2,12,1891],[10,9,4138],[11,3,2007],[1,10,9390],[12,8,1915],[6,2,1098],[5,4,2795],[3,13,4562],[9,7,9202],[4,6,6752],[8,11,1480],[7,5,9827]]
s = Solution()
print(s.minScore(n, nums))
