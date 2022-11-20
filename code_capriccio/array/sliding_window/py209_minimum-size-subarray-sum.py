
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start_idx, end_idx = 0, 0
        len_nums = len(nums)
        cur_sum = 0
        ans = len_nums + 1
        while end_idx < len_nums:
            cur_sum += nums[end_idx]
            while cur_sum >= target:
                ans = min(ans, end_idx - start_idx + 1)
                cur_sum -= nums[start_idx]
                start_idx += 1

            end_idx += 1

        return ans if ans < len_nums + 1 else 0


target = 7
nums = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(target, nums))