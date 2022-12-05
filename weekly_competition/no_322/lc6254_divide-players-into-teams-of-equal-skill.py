from collections import Counter

class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        sum_skill = sum(skill)
        n = len(skill)
        mean = sum_skill // (n // 2)
        if sum_skill % mean != 0:
            return -1

        ans = 0
        cnt = Counter(skill)
        for num in cnt:
            if cnt[num] != cnt[mean - num]:
                return -1
            elif cnt[num] > 0 and cnt[mean - num] > 0:
                num_of_groups = cnt[num]
                if num == (mean - num):
                    if cnt[num] % 2 != 0:
                        return -1
                    else:
                        num_of_groups = cnt[num] // 2
                ans += num * (mean - num) * num_of_groups
                cnt[num] = 0
                cnt[mean - num] = 0


        return -1 if ans == 0 else ans

nums = [15,6,19,10,4,14,8,20,2,7]
s = Solution()
print(s.dividePlayers(nums))
