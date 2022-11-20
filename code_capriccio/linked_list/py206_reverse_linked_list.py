
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 递归
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        def reverse(prev: ListNode, cur: ListNode):
            if not cur:
                return prev
            p = cur.next
            cur.next = prev
            return reverse(cur, p)
        return reverse(None, head)
    # 迭代
    # def reverseList(self, head: [ListNode]) -> [ListNode]:
    #     prev, cur = None, head
    #     while cur:
    #         p = cur.next
    #         cur.next = prev
    #         prev, cur = cur, p
    #
    #     return prev

