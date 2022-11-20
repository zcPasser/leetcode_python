"""
1、整型数组 nums。
2、数组中找出由三个数组成的最大乘积，并输出这个乘积。

返回：
    输出乘积。
"""
import sys


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        min1, min2 = sys.maxsize, sys.maxsize
        max1, max2, max3 = -sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1
        for num in nums:
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num >max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)
        # nums.sort()
        # return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])




s = Solution()
# nums = [-710,-107,-851,657,-14,-859,278,-182,-749,718,-640,127,-930,-462,694,969,143,309,904,-651,160,451,-159,-316,844,-60,611,-169,-73,721,-902,338,-20,-890,-819,-644,107,404,150,-219,459,-324,-385,-118,-307,993,202,-147,62,-94,-976,-329,689,870,532,-686,371,-850,-186,87,878,989,-822,-350,-948,-412,161,-88,-509,836,-207,-60,771,516,-287,-366,-512,509,904,-459,683,-563,-766,-837,-333,93,893,303,908,532,-206,990,280,826,-13,115,-732,525,-939,-787]
nums = [1, 2, 3]
print(s.maximumProduct(nums))