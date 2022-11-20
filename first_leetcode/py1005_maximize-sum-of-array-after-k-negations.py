from collections import Counter


class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        cnt = Counter(nums)
        ans = sum(nums)
        for i in range(-100, 0):
            if cnt[i]:
                ops = min(k, cnt[i])
                ans += -i * 2 * ops
                cnt[i] -= ops
                cnt[-i] += ops
                k -= ops
                if k <= 0:
                    break
        if k > 0 and k % 2 == 1 and not cnt[0]:
            for i in range(1, 101):
                if cnt[i]:
                    ans -= i * 2
                    break
        return ans
        # nums.sort()
        # idx_max_negative, len_nums = -1, len(nums)
        # for idx, num in enumerate(nums):
        #     if num < 0:
        #         idx_max_negative = idx
        # # no negatives in nums
        # if idx_max_negative == -1:
        #     if k % 2 == 1:
        #         nums[0] = -nums[0]
        # else:
        #     i = 0
        #     while k > 0 and i <= idx_max_negative:
        #         nums[i] = -nums[i]
        #         i, k = i + 1, k - 1
        #     # positives and still need to process
        #     if k > 0 and k % 2 == 1:
        #         if idx_max_negative < len_nums - 1:
        #             idx_max_negative = idx_max_negative if nums[idx_max_negative] < nums[idx_max_negative + 1] \
        #                 else idx_max_negative + 1
        #         nums[idx_max_negative] = -nums[idx_max_negative]
        #
        # return sum(nums)


nums = [2,-3,-1,5,-4]
k = 2
s = Solution()
print(s.largestSumAfterKNegations(nums, k))
