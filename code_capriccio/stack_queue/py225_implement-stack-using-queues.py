from collections import deque


class MyStack:

    def __init__(self):
        self.in_que = deque()
        self.out_que = deque()

    def push(self, x: int) -> None:
        self.in_que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        len_in_que = len(self.in_que)
        for _ in range(len_in_que - 1):
            self.out_que.append(self.in_que.popleft())

        self.in_que, self.out_que = self.out_que, self.in_que

        return self.out_que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.in_que[-1]

    def empty(self) -> bool:
        return not self.in_que



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()