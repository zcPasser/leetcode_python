


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        idx_of_even, idx_of_odd = 0, 1
        len_of_nums = len(nums)

        while idx_of_odd < len_of_nums and idx_of_even < len_of_nums:
            while idx_of_even < len_of_nums and nums[idx_of_even] % 2 == 0:
                idx_of_even += 2
            while idx_of_odd < len_of_nums and nums[idx_of_odd] % 2 == 1:
                idx_of_odd += 2
            if idx_of_odd < len_of_nums and idx_of_even < len_of_nums:
                nums[idx_of_even], nums[idx_of_odd] = nums[idx_of_odd], nums[idx_of_even]

        return nums


nums = [1, 2]
s = Solution()
print(s.sortArrayByParityII(nums))