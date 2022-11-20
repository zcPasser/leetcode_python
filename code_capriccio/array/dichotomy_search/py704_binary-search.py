

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] <target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


nums = [-1,0,3,5,9,12]
s = Solution()
print(s.search(nums, 13))