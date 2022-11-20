

class Solution(object):
    # def nextGreaterElement(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     len1, len2 = len(nums1), len(nums2)
    #     res = []
    #     for num in nums1:
    #         i = 0
    #         for j, x in enumerate(nums2):
    #             if x == num:
    #                 i = j
    #                 break
    #         flag = False
    #         for j in range(i + 1, len2):
    #             if nums2[j] > num:
    #                 flag = True
    #                 res.append(nums2[j])
    #                 break
    #         if not flag:
    #             res.append(-1)
    #
    #     return res

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]

