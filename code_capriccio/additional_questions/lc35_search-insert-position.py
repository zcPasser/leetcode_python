class Solution:
    # 二分法
    def searchInsert(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        left, right = 0, len_nums - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return right + 1
    # 暴力法
    # def searchInsert(self, nums: list[int], target: int) -> int:
    #     len_nums = len(nums)
    #     for i in range(len_nums):
    #         if nums[i] >= target:
    #             return i
    #     return len_nums