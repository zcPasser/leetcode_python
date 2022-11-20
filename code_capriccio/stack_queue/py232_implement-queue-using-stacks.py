class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        # 代码 复用，而不是 将 类似逻辑 代码 再搞一遍。
        # 工业代码 开发 习惯，尽量 复用，乃至 抽象出 功能相近 的 函数。
        ans = self.pop()
        self.out_stack.append(ans)

        return ans

    def empty(self) -> bool:
        return not self.out_stack and not self.in_stack



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()