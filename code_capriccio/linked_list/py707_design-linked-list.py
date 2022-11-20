class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        # 维护 虚拟头节点 和 计数器
        self._dummy_head = Node(-1)
        self._cnt = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._cnt:
            p = self._dummy_head
            for _ in range(index + 1):
                p = p.next
            return p.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._cnt, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self._cnt:
            p = self._dummy_head
            loop = min(index, self._cnt)
            for _ in range(loop):
                p = p.next
            cur_node = Node(val)
            if index == self._cnt:
                p.next = cur_node
            else:
                cur_node.next = p.next
                p.next = cur_node
            self._cnt += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._cnt:
            p = self._dummy_head
            for _ in range(index):
                p = p.next

            p.next = p.next.next
            self._cnt -= 1




# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# [1], [3], [1, 2], [1], [1], [1]
# param_1 = obj.get(index)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.deleteAtIndex(1)