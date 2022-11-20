
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 相遇
            if fast == slow:
                idx_1, idx_2 = head, fast
                while idx_1 != idx_2:
                    idx_1 = idx_1.next
                    idx_2 = idx_2.next
                return idx_1

        return None
        # hash_set = set()
        # p = head
        # while p:
        #     if p in hash_set:
        #         return p
        #     else:
        #         hash_set.add(p)
        #         p = p.next
        #
        # return None