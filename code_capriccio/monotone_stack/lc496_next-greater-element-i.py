class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        map_val_idx = dict()
        len_nums1, len_nums2 = len(nums1), len(nums2)
        for i in range(len_nums1):
            map_val_idx[nums1[i]] = i
        mono_stack = [0]
        ans = [-1 for _ in range(len_nums1)]
        for i in range(1, len_nums2):
            if nums2[i] <= nums2[mono_stack[-1]]:
                mono_stack.append(i)
            else:
                while len(mono_stack) > 0 and nums2[i] > nums2[mono_stack[-1]]:
                    if nums2[mono_stack[-1]] in map_val_idx:
                        ans[map_val_idx[nums2[mono_stack[-1]]]] = nums2[i]
                    mono_stack.pop()
                mono_stack.append(i)

        return ans