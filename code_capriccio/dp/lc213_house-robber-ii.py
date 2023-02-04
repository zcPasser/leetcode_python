class Solution:
    def rob(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums == 1:
            return nums[0]
        ans1 = self.rob_range(nums, 0, len_nums - 2, len_nums)
        ans2 = self.rob_range(nums, 1, len_nums - 1, len_nums)
        return max(ans1, ans2)

    def rob_range(self, nums, start, end, len_nums) -> int:
        if start == end:
            return nums[start]
        dp = [0] * (len_nums + 1)
        dp[start] = nums[start]
        dp[start + 1] = max(nums[start + 1], nums[start])
        for i in range(start + 2, end + 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[end]

nums = [1,2,3,1]
s = Solution()
print(s.rob(nums))