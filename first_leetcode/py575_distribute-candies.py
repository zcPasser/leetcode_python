"""
1、n 枚糖，其中第 i 枚糖的类型为 candyType[i] 。
2、吃掉 n / 2 枚糖，仅吃掉 n / 2 枚糖的情况下，能吃到糖的 最多 种类。

返回：
    吃到糖的 最多 种类数。
"""


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
        # eat_len = (len(candyType) // 2)
        # types = set()
        # ans = 0
        # for cur_type in candyType:
        #     if ans == eat_len:
        #         return eat_len
        #     if cur_type not in types:
        #         types.add(cur_type)
        #         ans += 1
        # return ans
