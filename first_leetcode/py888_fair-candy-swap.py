"""
description:
    1、given two integer arrays aliceSizes and bobSizes
        where aliceSizes[i] is the number of candies of the ith box of candy that Alice has
        and bobSizes[j] is the number of candies of the jth box of candy that Bob has.
    2、they would like to exchange one candy box each so that after the exchange,
        they both have the same total amount of candy.

return:
    Return an integer array answer
        where answer[0] is the number of candies in the box that Alice must exchange,
        and answer[1] is the number of candies in the box that Bob must exchange.


"""


class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_of_alice, sum_of_bob = sum(aliceSizes), sum(bobSizes)
        diff = (sum_of_alice + sum_of_bob) // 2 - sum_of_alice

        bobSizes = set(bobSizes)
        for size in aliceSizes:
            if (size + diff) in bobSizes:
                return [size, size + diff]
        return []
        # sum_of_alice, sum_of_bob = sum(aliceSizes), sum(bobSizes)
        # len_of_alice, len_of_bob = len(aliceSizes), len(bobSizes)
        # diff = (sum_of_alice + sum_of_bob) / 2 - sum_of_alice
        #
        # bobSizes.sort()
        # for size in aliceSizes:
        #     l, r = 0, len_of_bob - 1
        #     while l <= r:
        #         mid = (r - l) // 2 + l
        #         if bobSizes[mid] == size + diff:
        #             return [size, bobSizes[mid]]
        #         elif bobSizes[mid] < size + diff:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #
        # return []


aliceSizes = [35,17,4,24,10]
bobSizes = [63, 21]
s = Solution()
print(s.fairCandySwap(aliceSizes, bobSizes))