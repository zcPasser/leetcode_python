import itertools


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_of_alphabet = {}
        for idx, ch in enumerate(order):
            order_of_alphabet[ch] = idx


        def compare_alien_str(s1: str, s2: str) -> int:
            """
            :param s1:
            :param s2:
            :return:
                > 0:  order(s1) > order(s2)
                = 0:  order(s1) == order(s2)
                < 0:  order(s1) < order(s2)
            """
            len_of_s1, len_of_s2 = len(s1), len(s2)
            m = min(len_of_s1, len_of_s2)
            for i in range(m):
                if order_of_alphabet[s1[i]] == order_of_alphabet[s2[i]]:
                    continue
                else:
                    return order_of_alphabet[s1[i]] - order_of_alphabet[s2[i]]

            return len_of_s1 - len_of_s2

        for i in range(len(words) - 1):
            if compare_alien_str(words[i], words[i + 1]) > 0:
                return False

        return True


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
s = Solution()
print(s.isAlienSorted(words, order))