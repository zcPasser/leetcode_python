
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        # 空链 或 1个节点
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pprev, prev, cur = dummy_head, head, head.next
        while True:
            tmp = cur.next
            # 断链、连链
            cur.next = prev
            prev.next = tmp
            pprev.next = cur
            # 更新
            pprev, prev = prev, tmp
            # 下一组为空 或 下一组只有1个节点
            if not tmp or not tmp.next:
                break
            else:
                cur = tmp.next
        return dummy_head.next