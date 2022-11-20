"""
给你两个整数数组nums1 和 nums2 ，请你以数组形式返回两数组的交集。
返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
可以不考虑输出结果的顺序。
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1_dict = dict()
        for num in nums1:
            if num in nums1_dict:
                nums1_dict[num] += 1
            else:
                nums1_dict[num] = 1
        ans = []
        for num in nums2:
            if num in nums1_dict and nums1_dict[num] > 0:
                ans.append(num)
                nums1_dict[num] -= 1
        return ans