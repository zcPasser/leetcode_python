from collections import deque

class Solution:
    class Myque:
        def __init__(self):
            # 由于 需要 队列 两边同时 执行出队操作，故 底层使用 deque容器。
            self.que = deque()

        def pop(self, val):
            # 当 窗口移动时，需要 出队的 元素 刚好为当前最大值，才出队。
            # 而 移出窗口的 为 非最大值元素，在 其他元素 push时，已经从队尾 出队。
            # 即 单调队列中 序列 严格单调。
            if self.que and self.que[0] == val:
                self.que.popleft()

        def push(self, val):
            # 当前元素val 入队，将 队尾元素 比其 小的 全部出队，直至队空 或者 遇到 比val大的。
            while self.que and self.que[-1] < val:
                self.que.pop()
            self.que.append(val)

        def peek(self):
            return self.que[0]

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        que = self.Myque()
        ans = []
        # 初始化窗口：先 入队 k个元素
        for i in range(k):
            que.push(nums[i])
        # 获取当前窗口 中 最大元素
        ans.append(que.peek())

        for i in range(k, len(nums)):
            # 移动窗口，移除左端元素。
            que.pop(nums[i - k])
            # 移入 右端元素
            que.push(nums[i])
            # 获取当前窗口最大元素
            ans.append(que.peek())
        return ans


nums = [1,3,1,2,0,5]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))