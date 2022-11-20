from math import lcm

class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            last_lcm = nums[i]
            for j in range(i, len(nums)):
                last_lcm = lcm(last_lcm, nums[j])
                if last_lcm > k:
                    break
                elif last_lcm == k:
                    ans += 1

        return ans




nums = [3,6,2,7,1]
k = 6
s = Solution()
print(s.subarrayLCM(nums, k))