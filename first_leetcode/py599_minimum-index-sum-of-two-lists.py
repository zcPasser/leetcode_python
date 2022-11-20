"""
1、2个list分别表示各自最喜爱的餐厅，元素为字符串形式的餐厅名。
2、用最少的索引和找出他们共同喜爱的餐厅。

返回：
    共同喜爱的餐厅名，不考虑顺序，可能不唯一。
"""
# import sys
import time


class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        if len(list1) > len(list2):
            short_list, long_list = list2, list1
        else:
            short_list, long_list = list1, list2
        name_to_idx1 = {name: idx for idx, name in enumerate(short_list)}
        min_sum_idxs = 2001
        ans = []
        for idx, name in enumerate(long_list):
            if name in name_to_idx1:
                temp_sum_idxs = idx + name_to_idx1[name]
                if temp_sum_idxs == min_sum_idxs:
                    ans.append(name)
                elif temp_sum_idxs < min_sum_idxs:
                    min_sum_idxs = temp_sum_idxs
                    ans.clear()
                    ans.append(name)
                else:
                    continue

        return ans

        # name_to_idx1 = {name: idx for idx, name in enumerate(list1)}
        # name_to_idx2 = {name: idx for idx, name in enumerate(list2)}
        # ans, min_sum_idxs = [], sys.maxsize
        # for name, idx in name_to_idx1.items():
        #     if name in name_to_idx2:
        #         sum_idxs = name_to_idx1[name] + name_to_idx2[name]
        #         ans.append((name, sum_idxs))
        #         # name_to_idx1[name] += name_to_idx2[name]
        #         min_sum_idxs = sum_idxs if min_sum_idxs > sum_idxs else min_sum_idxs
        #
        # return [name for (name, sum_idxs) in ans if sum_idxs == min_sum_idxs]


s = Solution()
l1 = ["Shogun","Tapioca Express","Burger King","KFC", 'sasa', 'sssss', 'scxfef', '111111', '2451', '正在系统', 'wsws']
l2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
sum_time = 0
n = 10000
for i in range(n):
    start_time = time.perf_counter()
    s.findRestaurant(l1, l2)
    # print(s.findRestaurant(l1, l2))
    sum_time += time.perf_counter() - start_time
print('lenght of average time:{0}'.format(sum_time / n))

