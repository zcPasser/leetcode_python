"""
1、一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
2、另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

返回：
    返回能否在剩下空间中根据条件再种植n朵。
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # len_flowerbed = len(flowerbed)
        # idx = 0
        # while idx < len_flowerbed:
        #     if flowerbed[idx] == 1:
        #         idx += 2
        #     elif idx == len_flowerbed - 1 or flowerbed[idx + 1] == 0:
        #         n -= 1
        #         if n <= 0:
        #             return True
        #         idx += 2
        #     else:
        #         idx += 3
        # return n <= 0

        if len(flowerbed) <= 0:
            return n == 0

        count_of_zero = 1
        can_planted_total = 0
        for bed in flowerbed:
            if bed == 0:
                count_of_zero += 1
            else:
                can_planted_total += (count_of_zero - 1) // 2
                if can_planted_total >= n:
                    return True
                count_of_zero = 0
        count_of_zero += 1
        can_planted_total += (count_of_zero - 1) // 2

        return can_planted_total >= n



s = Solution()
f = [0,0,1,0,0]
n = 2
print(s.canPlaceFlowers(f, n))