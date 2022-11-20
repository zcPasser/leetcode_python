

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        cnt = set()
        for num in nums:
            if num in cnt:
                return num
            else:
                cnt.add(num)
        return -1
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        #
        # return -1