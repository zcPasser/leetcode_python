

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt = [0] * 1001
        for num in nums1:
            cnt[num] += 1
        ans = []
        for num in nums2:
            if cnt[num] > 0:
                cnt[num] -= 1
                ans.append(num)

        return ans