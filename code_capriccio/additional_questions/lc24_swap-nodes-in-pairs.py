# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next and cur.next.next:
            tmp1 = cur.next
            tmp2 = cur.next.next

            cur.next = tmp2
            tmp1.next = tmp2.next
            tmp2.next = tmp1

            cur = tmp1
        return dummy_head.next