"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    # 结合 头插入。
    def reverseList(self, head: ListNode) -> ListNode:
        # 空链。
        if not head:
            return head
        # p：用来遍历的指针；curr_head：用来指向当前头节点。
        p, curr_head = head.next, head
        while p:
            # 暂存 p的 下一个节点，避免丢失。
            q = p.next
            # 断链，头插入。
            p.next, curr_head = curr_head, p
            # p 继续遍历。
            p = q
        # head重新指向，
        head.next, head = None, curr_head
        return head


head = ListNode(1)
p = ListNode(2)
head.next = p

ss = Solution()
ss.reverseList(head)