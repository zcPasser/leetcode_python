import sys

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = -sys.maxsize - 1
        cnt = 0
        for num in nums:
            cnt += num
            ans = max(ans, cnt)
            if cnt <= 0:
                cnt = 0
        return ans