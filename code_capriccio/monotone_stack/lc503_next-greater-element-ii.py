class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        ans = [-1 for _ in range(len_nums)]
        mono_stack = [0]
        for i in range(1, len_nums * 2):
            if nums[i % len_nums] <= nums[mono_stack[-1]]:
                mono_stack.append(i % len_nums)
            else:
                while len(mono_stack) > 0 and nums[i % len_nums] > nums[mono_stack[-1]]:
                    ans[mono_stack[-1]] = nums[i % len_nums]
                    mono_stack.pop()
                mono_stack.append(i % len_nums)
        return ans


nums = [1,2,1]
s = Solution()
print(s.nextGreaterElements(nums))