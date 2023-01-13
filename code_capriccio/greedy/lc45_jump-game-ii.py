class Solution:
    def jump(self, nums: list[int]) -> int:
        len_nums = len(nums)
        cur_dist = 0
        ans = 0
        end = 0
        for i in range(len_nums - 1):
            cur_dist = max(nums[i] + i, cur_dist)
            if i == end:
                end = cur_dist
                ans += 1
        return ans