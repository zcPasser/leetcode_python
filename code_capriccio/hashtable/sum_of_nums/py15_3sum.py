

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        len_nums = len(nums)
        if len_nums < 3:
            return []
        # 排序 预处理。
        nums.sort()
        ans = []
        for i in range(len_nums):
            # i 指针 指向 有序三元组 中 最小，若 最小为 正数，则 有序序列 剩余 不含有 合法 结果。
            if nums[i] > 0:
                return ans
            # 对 三元组 a+b+c=0 中 的 a 去重
            # 注意 是 i 和 i-1 比较，是 组间 去重，而非 组内 去重。
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针 各自 初始位置。
            left, right = i + 1, len_nums - 1
            while left < right:
                sum_cur = nums[i] + nums[left] + nums[right]
                if sum_cur > 0:
                    right -= 1
                elif sum_cur < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 分别 对 b、c去重，结合 有序序列，left、right指针 往中间 移动。
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 还需要 多走 一步
                    left += 1
                    right -= 1
        return ans

    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     # 如果 nums 个数 < 3，肯定组不成三元组
    #     if len(nums) < 3:
    #         return []
    #     # 对 nums 进行排序，这样在后面的时候可以减少重复带来的问题
    #     nums.sort()
    #     # res 存储最后的结果，set 集合的特点是无序且无重复
    #     res = set()
    #
    #     for i in range(len(nums)):
    #         # 元素去重
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #
    #         # 初始化哈希表。
    #         hash = {}
    #         for j in range(i + 1, len(nums)):
    #             # 如果不在哈希表中，加入哈希表
    #             if nums[j] not in hash:
    #                 hash[-nums[i] - nums[j]] = 1
    #             # 如果在哈希表中，则存在三元组
    #             else:
    #                 res.add((nums[i], -nums[i] - nums[j], nums[j]))
    #
    #     return list(res)



nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))