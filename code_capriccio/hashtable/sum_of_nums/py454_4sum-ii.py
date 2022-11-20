import collections

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        map_1 = dict()
        for num1 in nums1:
            for num2 in nums2:
                if (num1 + num2) in map_1:
                    map_1[num1 + num2] += 1
                else:
                    map_1[num1 + num2] = 1
        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                if (-num3 - num4) in map_1:
                    ans += map_1[-num3 - num4]
        return ans


nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
s = Solution()
print(s.fourSumCount(nums1, nums2, nums3, nums4))