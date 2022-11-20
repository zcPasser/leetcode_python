"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next, p = head, dummy_head
        while p.next:
            # 当前节点 不符合删除条件。
            if p.next.val != val:
                p = p.next
            # 当前节点 满足删除条件。
            else:
                p.next = p.next.next

        return dummy_head.next


head = ListNode(2)
p1 = ListNode(2)
head.next = p1
ss = Solution()
ss.removeElements(head, 2)