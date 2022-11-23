from collections import Counter

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        ans = 0
        cnt = Counter(nums)
        keys = list(cnt.keys())
        len_keys = len(keys)
        for i in range(len_keys):
            for j in range(i + 1, len_keys):
                for k in range(j + 1, len_keys):
                    ans += cnt[keys[i]] * cnt[keys[j]] * cnt[keys[k]]
        return ans


nums = [1,1,1,1,1]
s = Solution()
print(s.unequalTriplets(nums))
