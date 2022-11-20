"""
1、一个整数数组 nums ，请计算数组的 中心下标 。
2、数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
    如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
    如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

返回：
    中心下标。
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_of_nums = sum(nums)
        pre_sum = 0
        for idx, num in enumerate(nums):
            if 2 * pre_sum == sum_of_nums - num:
                return idx
            pre_sum += num
        return -1
        # len_of_nums = len(nums)
        # pre_sum = [0] * (len_of_nums + 1)
        # for idx in range(1, len_of_nums + 1):
        #     pre_sum[idx] = pre_sum[idx - 1] + nums[idx - 1]
        # for idx in range(0, len_of_nums):
        #     if pre_sum[idx] == (pre_sum[len_of_nums] - pre_sum[idx + 1]):
        #         return idx
        # return -1


s = Solution()
nums = [1,7,3,6,5,6]
print(s.pivotIndex(nums))