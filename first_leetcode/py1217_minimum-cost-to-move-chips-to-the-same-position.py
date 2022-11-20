
class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # sum_chips = len(position)
        # if sum_chips == 1:
        #     return 0
        cnt = [0, 0]
        for pos in position:
            cnt[pos % 2] += 1
        return min(cnt)
        # costs = [0] * (sum_chips + 1)
        # for idx, num in enumerate(position):
        #     for j in range(1, sum_chips + 1):
        #         if abs(num - j) % 2 == 1:
        #             costs[j] += 1
        #
        #
        # return min(costs[1:])


position = [1000000000]
s = Solution()
print(s.minCostToMoveChips(position))