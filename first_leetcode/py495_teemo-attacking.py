"""
当提莫攻击艾希，艾希的中毒状态正好持续duration 秒。

正式地讲，提莫在 t 发起发起攻击意味着艾希在时间区间 [t, t + duration - 1]（含 t 和 t + duration - 1）处于中毒状态。
如果提莫在中毒影响结束 前 再次攻击，中毒状态计时器将会 重置 ，在新的攻击之后，中毒影响将会在 duration 秒后结束。

给你一个 非递减 的整数数组 timeSeries ，其中 timeSeries[i] 表示提莫在 timeSeries[i] 秒时对艾希发起攻击，以及一个表示中毒持续时间的整数 duration 。

返回艾希处于中毒状态的 总 秒数。
"""


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # timeSeries_len = len(timeSeries)
        # i, j = 1, 0
        # res, one_time = 0, 0
        # if duration == 0 or not timeSeries:
        #     return res
        # flag = False
        # while j < timeSeries_len:
        #     if i == timeSeries[j]:
        #         res += one_time
        #         one_time = 0
        #         j += 1
        #         flag = True
        #     elif one_time == duration:
        #         res += duration
        #         one_time = 0
        #         flag = False
        #     if flag:
        #         one_time += 1
        #
        #     i += 1
        #
        # return res + duration
        ans, expired = 0, 0
        for i in range(len(timeSeries)):
            if timeSeries[i] >= expired:
                ans += duration
            else:
                ans += timeSeries[i] + duration - expired
            expired = timeSeries[i] + duration
        return ans


time = [1, 2]
d = 2
ss = Solution()
print(ss.findPoisonedDuration(time, d))