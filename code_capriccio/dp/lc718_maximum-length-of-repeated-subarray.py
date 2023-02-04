class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        len_nums1, len_nums2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(len_nums2 + 1)] for _ in range(len_nums1 + 1)]
        ans = 0
        for i in range(1, len_nums1 + 1):
            for j in range(1, len_nums2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                ans = max(ans, dp[i][j])
        return ans