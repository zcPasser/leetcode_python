
class Solution:
    # 线性时间算法，不使用额外空间。
    # 位运算
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
