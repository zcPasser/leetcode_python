
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        len_nums = len(nums)
        left_idx, right_idx = 0, len_nums - 1
        while left_idx <= right_idx:
            while left_idx < len_nums and nums[left_idx] != val:
                left_idx += 1
            while right_idx < len_nums and nums[right_idx] == val:
                right_idx -= 1
            if left_idx < right_idx:
                nums[left_idx] = nums[right_idx]
                left_idx, right_idx = left_idx + 1, right_idx - 1

        return left_idx
        # fast_idx, slow_idx = 0, 0
        # len_nums = len(nums)
        # while fast_idx < len_nums:
        #     if nums[fast_idx] != val:
        #         nums[slow_idx] = nums[fast_idx]
        #         slow_idx += 1
        #     fast_idx += 1
        #
        # return slow_idx


nums = [0,1,2,2,3,0,4,2]
val = 2
s = Solution()
print(nums)
print(s.removeElement(nums, val))
print(nums)
