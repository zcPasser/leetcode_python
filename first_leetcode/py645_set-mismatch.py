"""
1、集合 s 包含从 1 到 n 的整数。
2、集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
3、给定一个数组 nums 代表了集合 S 发生错误后的结果。

返回：
    找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
"""


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        cur_total = sum(nums)
        ans = []
        for num in nums:
            nums[(num - 1) % n] += n
        for idx, num in enumerate(nums):
            if num > 2 * n:
                ans.append(idx + 1)
                break
        ans.append(((1 + n) * n // 2) - cur_total + ans[0])
        return ans


nums = [3, 2, 2]
s = Solution()
print(s.findErrorNums(nums))