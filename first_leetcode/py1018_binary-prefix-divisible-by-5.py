

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        prefix = 0
        for num in nums:
            prefix = ((prefix << 1) + num) % 5
            ans.append(prefix == 0)

        return ans


nums = [1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0]
s = Solution()
print(s.prefixesDivBy5(nums))