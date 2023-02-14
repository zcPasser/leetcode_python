class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums
        dp = [1 for _ in range(len_nums)]
        cnt = [1 for _ in range(len_nums)]
        max_len = 1
        for i in range(1, len_nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
                if dp[i] > max_len:
                    max_len = dp[i]
        ans = 0
        for i in range(len_nums):
            if dp[i] == max_len:
                ans += cnt[i]
        return ans

nums = [1,3,5,4,7]
s = Solution()
print(s.findNumberOfLIS(nums))