class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        len_nums = len(nums)
        # smaller_set, bigger_set = set(range(1, k)), set(range(k, len_nums + 1))
        center = nums.index(k)
        smaller_nums, bigger_nums = 0, 0
        if center == 0:
            for right in range(center, len_nums):
                if nums[right] > k:
                    bigger_nums += 1
                else:
                    smaller_nums += 1
                if smaller_nums == bigger_nums or bigger_nums - smaller_nums == 1:
                    ans += 1
        else:
            nums_set = set()
            for left in range(center, -1, -1):
                for right in range(center, len_nums):
                    if nums[right] not in nums_set:
                        pass
                    if nums[right] > k:
                        bigger_nums += 1
                    else:
                        smaller_nums += 1
                    if smaller_nums == bigger_nums or bigger_nums - smaller_nums == 1:
                        ans += 1
        return ans

nums = [2,3,1]
k = 3
s = Solution()
print(s.countSubarrays(nums, k))