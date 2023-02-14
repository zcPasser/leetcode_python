class Solution:
    def bit_cnt(self, n):
        ans = 0
        while n > 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1
        return ans

    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda n: (self.bit_cnt(n), n))
        return arr