

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left_idx, right_idx = 0, len(nums) - 1
        ans = [0] * (right_idx + 1)
        idx = right_idx
        while idx >= 0:
            x, y = nums[left_idx] ** 2, nums[right_idx] ** 2
            if x < y:
                ans[idx] = y
                right_idx -= 1
            else:
                ans[idx] = x
                left_idx += 1
            idx -= 1

        return ans