class Solution:
    def canJump(self, nums: list[int]) -> bool:
        len_nums = len(nums)
        if len_nums < 2:
            return True
        coverage = 0
        i = 0
        while i <= coverage:
            coverage = max(i + nums[i], coverage)
            if coverage >= len_nums - 1:
                return True
            i += 1
        return False