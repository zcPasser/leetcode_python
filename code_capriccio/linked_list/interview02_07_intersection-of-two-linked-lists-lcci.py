
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA

        return p