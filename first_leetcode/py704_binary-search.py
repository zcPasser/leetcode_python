"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，
写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

"""


class Solution:
    # 二分查找。
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
