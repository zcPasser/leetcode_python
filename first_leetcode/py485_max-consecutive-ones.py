class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, one_time = 0, 0

        for num in nums:
            if num == 1:
                one_time += 1
            else:
                ans = max(ans, one_time)
                one_time = 0

        return max(ans, one_time)