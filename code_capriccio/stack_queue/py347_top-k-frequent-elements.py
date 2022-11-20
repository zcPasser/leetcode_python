from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 解决 频率计数——map映射 。
        cnt = Counter(nums)
        # 频率排序——
        # 优先级队列——小顶堆。
        pri_que = []
        # 维护长度 为 k的 小顶堆。
        for key, val in cnt.items():
            heapq.heappush(pri_que, (val, key))
            # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        # 前 K个 高频元素
        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        ans = [0] * k
        for idx in range(k - 1, -1, -1):
            ans[idx] = heapq.heappop(pri_que)[1]
        return ans