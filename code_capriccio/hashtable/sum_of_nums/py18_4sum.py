
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        len_nums = len(nums)
        if len_nums < 4:
            return []
        ans = []
        nums.sort()
        for k in range(len_nums - 3):
            # 剪枝
            if nums[k] > target and nums[k] >= 0:
                break
            # 对 nums[k] 去重
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 确定 nums[k]后，开始 确定 nums[i]
            for i in range(k + 1, len_nums - 2):
                cur_nums = nums[k] + nums[i]
                # 剪枝
                if cur_nums > target and cur_nums >= 0:
                    break
                # 对 nums[i] 去重
                if i > (k + 1) and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, len_nums - 1
                while left < right:
                    cur_sum = cur_nums + nums[left] + nums[right]
                    if cur_sum > target:
                        right -= 1
                    elif cur_sum < target:
                        left += 1
                    else:
                        # 收获 合法 结果
                        ans.append([nums[k], nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return ans


nums = [-1,0,1,2,-1,-4]
target = -1
s = Solution()
print(s.fourSum(nums, target))