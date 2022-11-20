

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        a, len_of_num = k, len(num)
        i = len_of_num - 1
        bit = 0
        while i >= 0:
            a, b = divmod(a, 10)
            bit, num[i] = divmod(num[i] + b + bit, 10)
            i -= 1
        ans = []
        while a > 0:
            a, b = divmod(a, 10)
            bit, b = divmod(b + bit, 10)
            ans.append(b)
        if bit == 1:
            ans.append(1)
        return ans[::-1] + num