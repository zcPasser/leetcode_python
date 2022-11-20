import collections


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        cnt1, cnt2 = {}, {}
        arr2_set = set(arr2)
        for num in arr1:
            if num in arr2_set:
                cnt1[num] = cnt1.get(num, 0) + 1
            else:
                cnt2[num] = cnt2.get(num, 0) + 1
        ans = []
        for num in arr2:
            ans.extend([num] * cnt1[num])

        for num in sorted(cnt2):
            ans.extend([num] * cnt2[num])

        return ans


arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
s = Solution()
print(s.relativeSortArray(arr1, arr2))