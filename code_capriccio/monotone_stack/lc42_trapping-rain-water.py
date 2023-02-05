class Solution:
    def trap(self, height: list[int]) -> int:
        len_h = len(height)
        ans = 0
        mono_stack = [0]
        for i in range(1, len_h):
            if height[mono_stack[-1]] > height[i]:
                mono_stack.append(i)
            elif height[mono_stack[-1]] == height[i]:
                mono_stack.pop()
                mono_stack.append(i)
            else:
                while len(mono_stack) > 0 and height[mono_stack[-1]] < height[i]:
                    mid = mono_stack.pop()
                    if len(mono_stack) > 0:
                        h = min(height[mono_stack[-1]], height[i]) - height[mid]
                        w = i - mono_stack[-1] - 1
                        ans += h * w
                mono_stack.append(i)
        return ans


