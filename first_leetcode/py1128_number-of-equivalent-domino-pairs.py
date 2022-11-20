

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans = 0
        nums = [0] * 100
        for x, y in dominoes:
            num = x * 10 + y if x < y else y * 10 + x
            ans += nums[num]
            nums[num] += 1

        return ans

        # ans = 0
        # d = {}
        # for domino in dominoes:
        #     if domino[0] > domino[1]:
        #         domino = [domino[1], domino[0]]
        #     s = tuple(domino)
        #     d[s] = d.get(s, 0) + 1
        # # 计算答案
        # for i in d:
        #     ans += d[i] * (d[i] - 1) // 2
        # return ans

        # def is_dominopair(domino1: tuple, domino2: tuple) -> bool:
        #     return (domino1[0] == domino2[0] and domino1[1] == domino2[1]) or \
        #            (domino1[0] == domino2[1] and domino1[1] == domino2[0])
        # len_dominoes = len(dominoes)
        # ans = 0
        # for i in range(len_dominoes - 1):
        #     for j in range(i + 1, len_dominoes):
        #         if is_dominopair(dominoes[i], dominoes[j]):
        #             ans += 1
        #
        # return ans

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
s = Solution()
print(s.numEquivDominoPairs(dominoes))