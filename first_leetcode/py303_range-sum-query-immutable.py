"""
给定一个整数数组 nums，处理以下类型的多个查询:

计算索引left和right（包含 left 和 right）之间的 nums 元素的 和 ，其中left <= right
实现 NumArray 类：

1、NumArray(int[] nums) 使用数组 nums 初始化对象
2、int sumRange(int i, int j) 返回数组 nums中索引left和right之间的元素的 总和 ，
包含left和right两点（也就是nums[left] + nums[left + 1] + ... + nums[right])
"""


class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.sums = [0]
        sum = 0
        for num in nums:
            sum += num
            self.sums.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]



# Your NumArray object will be instantiated and called as such:
nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
param_1 = obj.sumRange(2, 5)
print(param_1)