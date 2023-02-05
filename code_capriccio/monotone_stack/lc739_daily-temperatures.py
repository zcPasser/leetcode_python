class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        len_temp = len(temperatures)
        ans = [0 for _ in range(len_temp)]
        mon_stack = [0]
        for i in range(1, len_temp):
            if temperatures[mon_stack[-1]] >= temperatures[i]:
                mon_stack.append(i)
            else:
                while len(mon_stack) > 0 and temperatures[mon_stack[-1]] < temperatures[i]:
                    ans[mon_stack[-1]] = i - mon_stack[-1]
                    mon_stack.pop()
                mon_stack.append(i)
        return ans