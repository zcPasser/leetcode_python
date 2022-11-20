"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

实现 MyStack 类：

void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

注意：

你只能使用队列的基本操作 —— 也就是push to back、peek/pop from front、size 和is empty这些操作。
你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。

"""


class MyStack:

    def __init__(self):
        # q1 主队列，q2 辅助队列。
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        q1_len = len(self.q1)
        self.q1.append(x)
        for i in range(q1_len):
            self.q2.append(self.q1.pop(0))
        for i in range(q1_len):
            self.q1.append(self.q2.pop(0))

    def pop(self) -> int:
        return self.q1.pop(0) if not self.empty() else None

    def top(self) -> int:
        return self.q1[0] if not self.empty() else None

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()