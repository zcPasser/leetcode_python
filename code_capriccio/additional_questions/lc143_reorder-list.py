# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: [ListNode]) -> [ListNode]:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp
        return pre

    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head1, head2 = head, slow.next
        slow.next = None
        head2 = self.reverse_list(head2)

        cur1, cur2 = head1, head2
        cnt = 0
        cur = head
        while cur2:
            tmp = cur.next
            cur.next = cur2
            cur = tmp

            tmp = cur2.next
            cur2.next = cur
            cur2 = tmp
