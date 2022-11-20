

from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        cnt = Counter(deck)
        return reduce(gcd, (v for v in cnt.values())) >= 2
        # card_to_cnt = {}
        # for card in deck:
        #     card_to_cnt[card] = card_to_cnt.get(card, 0) + 1
        #
        # def gcd(a: int, b: int):
        #     if a < b:
        #         a, b = b, a
        #     elif a == b:
        #         return a
        #
        #     while a % b != 0:
        #         a, b = b, a % b
        #
        #     return b
        #
        # cnts = list(card_to_cnt.values())
        # len_of_cnts = len(cnts)
        # if len_of_cnts < 2:
        #     return cnts[0] >= 2
        #
        # cur_gcd = gcd(cnts[0], cnts[1])
        # for i in range(2, len_of_cnts):
        #     cur_gcd = gcd(cur_gcd, cnts[i])
        #
        # return cur_gcd >= 2


deck = [1]
s = Solution()
print(s.hasGroupsSizeX(deck))