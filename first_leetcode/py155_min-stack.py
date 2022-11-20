"""
    实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini_list) == 0:
            self.mini_list.append(val)
        else:
            self.mini_list.append(min(val, self.mini_list[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.mini_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_list[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()