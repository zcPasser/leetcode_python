
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 处理 返回新头节点 问题。
        ans = ListNode(0, head)
        # 指针记录。
        p = ans
        while p.next:
            # 一直遍历到 不为 val 的 节点。
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return ans.next
