class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        len_h = len(heights)
        ans = 0
        mono_stack = [0]
        for i in range(1, len_h):
            if heights[mono_stack[-1]] < heights[i]:
                mono_stack.append(i)
            elif heights[mono_stack[-1]] == heights[i]:
                mono_stack.pop()
                mono_stack.append(i)
            else:
                while len(mono_stack) > 0 and heights[mono_stack[-1]] > heights[i]:
                    mid = mono_stack.pop()
                    if len(mono_stack) > 0:
                        h = heights[mid]
                        w = i - mono_stack[-1] - 1
                        ans = max(h * w,  ans)
                mono_stack.append(i)
        return ans

h = [2,4]
s = Solution()
print(s.largestRectangleArea(h))