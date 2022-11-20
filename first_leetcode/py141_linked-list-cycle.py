# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 边界：空链表 或 单个节点 。——可以合并。
        # if not head:
        #     return False
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next

        return False


head = ListNode(3)
p = ListNode(2)
head.next = p
q = ListNode(0)
p.next = q
z = ListNode(-4)
q.next = z
z.next = p

ss = Solution()
print(ss.hasCycle(head))


