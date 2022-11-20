
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        slow, fast = dummy_head, dummy_head
        while n != 0:   # fast先往前走n步
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        # fast 走到结尾后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next  # 删除

        return dummy_head.next

