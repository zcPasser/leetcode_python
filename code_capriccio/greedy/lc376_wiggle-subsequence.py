class Solution:
    # dp
    def wiggleMaxLength(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums
        dp = [[0, 0] for _ in range(len_nums)]
        dp[0][0], dp[0][1] = 1, 1
        for i in range(1, len_nums):
            dp[i][0], dp[i][1] = 1, 1
            for j in range(i):
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[len_nums - 1][0], dp[len_nums - 1][1])
    # greedy
    # def wiggleMaxLength(self, nums: list[int]) -> int:
    #     len_nums = len(nums)
    #     if len_nums <= 1:
    #         return len_nums
    #     ans = 1
    #     cur_diff = 0
    #     pre_diff = 0
    #     for i in range(len_nums - 1):
    #         cur_diff = nums[i + 1] - nums[i]
    #         if (cur_diff > 0 and pre_diff <= 0) or (cur_diff < 0 and pre_diff >= 0):
    #             ans += 1
    #             pre_diff = cur_diff
    #     return ans
