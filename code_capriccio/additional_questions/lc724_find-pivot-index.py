class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_nums = sum(nums)
        left_sum, right_sum = 0, 0
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum = sum_nums - left_sum + nums[i]
            if left_sum == right_sum:
                return i
        return -1