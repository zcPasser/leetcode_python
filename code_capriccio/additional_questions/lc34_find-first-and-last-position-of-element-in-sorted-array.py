class Solution:
    def get_left_border(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        left_border = -2
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] >= target:
                right = mid - 1
                left_border = right
            else:
                left = mid + 1

        return left_border

    def get_right_border(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        right_border = -2
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                right_border = left
        return right_border

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        len_nums = len(nums)
        left_border, right_border = self.get_left_border(nums, target), self.get_right_border(nums, target)

        if left_border == -2 or right_border == -2:
            return [-1, -1]
        if right_border - left_border > 1:
            return [left_border + 1, right_border - 1]
        return [-1, -1]