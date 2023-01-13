class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        ans = 0
        cur_sum = 0
        total_sum = 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:
                ans = i + 1
                cur_sum = 0

        return ans if total_sum >= 0 else -1

gas = [3, 1, 1]
cost = [1, 2, 2]
s = Solution()
print(s.canCompleteCircuit(gas, cost))