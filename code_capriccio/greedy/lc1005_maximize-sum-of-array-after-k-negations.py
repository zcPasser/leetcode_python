class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        def cmp(a):
            return abs(a)
        len_nums = len(nums)
        nums.sort(key=cmp, reverse=True)
        for i in range(len_nums):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            else:
                break
        if k > 0:
            nums[-1] = nums[-1] if k % 2 == 0 else -nums[-1]
        return sum(nums)

nums = [4,2,3]
k = 1
s = Solution()
print(s.largestSumAfterKNegations(nums, k))
