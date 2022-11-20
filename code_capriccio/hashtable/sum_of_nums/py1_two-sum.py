

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pool = dict()
        for idx, num in enumerate(nums):
            if (target - num) in pool:
                return [pool[target - num], idx]
            else:
                pool[num] = idx

        return []