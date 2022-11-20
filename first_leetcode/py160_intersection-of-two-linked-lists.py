"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
如果两个链表不存在相交节点，返回 null 。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
        链表headA 和 headB 的长度分别是 m 和 n。
        假设链表 headA 的不相交部分有 a个节点，链表 headB 的不相交部分有 b 个节点，两个链表相交的部分有 c 个节点，
        则有 a + c = m，b + c = n。
    """

    # 核心：两条链表，2个指针，不同出发点，同时走一遍 两条链表，若是有相交处，相遇2次，无相交处，相遇一次，即为None。
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 边界：存在 空链表。
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
    # 相交，则必存在 从某处开始节点地址一直相同。
    # 当链表A走到最后，从B开始遍历，若在A存在相同节点，则满足条件。
    # 核心：相同问题，借助哈希。
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     # 边界：存在 空链表。
    #     if not headA or not headB:
    #         return None
    #     hash_a_set = set()
    #     p, q = headA, headB
    #     while p:
    #         hash_a_set.add(p)
    #         p = p.next
    #
    #     while q:
    #         if q in hash_a_set:
    #             return q
    #         q = q.next
    #     return None
    # 相交，则必存在 从某处开始节点地址一直相同。
    # 当链表A和链表B都走到最后，相交时必定地址相同，一直回溯到地址不同的时刻，其最后一次相同的时刻即相交处。
    # 核心：回溯——借助 栈。
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     # 边界：存在 空链表。
    #     if not headA or not headB:
    #         return None
    #
    #     stack_A_list = []
    #     stack_B_list = []
    #     p, q = headA, headB
    #     while p:
    #         stack_A_list.append(p)
    #         p = p.next
    #     while q:
    #         stack_B_list.append(q)
    #         q = q.next
    #     insert_node = None
    #     while len(stack_A_list) > 0 and len(stack_B_list) > 0 and stack_A_list[-1] == stack_B_list[-1]:
    #         insert_node = stack_A_list.pop()
    #         stack_B_list.pop()
    #
    #     return insert_node
