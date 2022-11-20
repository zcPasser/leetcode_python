import collections


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ans = 0
        start_idx, end_idx = 0, 0
        baskets = collections.Counter()
        while end_idx < len(fruits):
            baskets[fruits[end_idx]] += 1
            while len(baskets) > 2:
                baskets[fruits[start_idx]] -= 1
                if baskets[fruits[start_idx]] == 0:
                    baskets.pop(fruits[start_idx])
                start_idx += 1
            ans = max(ans, end_idx - start_idx + 1)
            end_idx += 1
        return ans


fruits = [1,2,3,2,2]
s  = Solution()
print(s.totalFruit(fruits))
