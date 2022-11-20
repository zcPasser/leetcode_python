

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        max_height = max(heights)
        buckets = [0] * (max_height + 1)
        for height in heights:
            buckets[height] += 1
        idx_heights = 0
        ans = 0
        for idx_buckets in range(1, max_height + 1):
            while buckets[idx_buckets] > 0:
                buckets[idx_buckets] -= 1
                if idx_buckets != heights[idx_heights]:
                    ans += 1
                idx_heights += 1
        return ans
        # len_heights = len(heights)
        # expected = sorted(heights)
        # ans = 0
        # for a, b in zip(expected, heights):
        #     if a != b:
        #         ans += 1
        # return ans


h = [1,2,3,4,5]
s = Solution()
print(s.heightChecker(h))