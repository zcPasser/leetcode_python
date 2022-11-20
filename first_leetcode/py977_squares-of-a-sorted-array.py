

class Solution:
    def sortedSquares(self, nums: list[int]) ->list[int]:
        left, right = 0, len(nums) - 1
        ans = [0] * (right + 1)
        idx_of_ans = right
        while idx_of_ans >= 0:
            a, b = nums[left] ** 2, nums[right] ** 2
            if a < b:
                ans[idx_of_ans] = b
                right -= 1
            else:
                ans[idx_of_ans] = a
                left += 1
            idx_of_ans -= 1

        return ans
        # nums.sort(key=lambda x: abs(x))
        # return [num ** 2 for num in nums]
