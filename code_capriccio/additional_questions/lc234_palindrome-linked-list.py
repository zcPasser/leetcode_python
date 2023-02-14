
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: [ListNode]) -> [ListNode]:
        node = None
        cur = head
        pre = None

        while cur:
            node = cur.next
            cur.next = pre
            pre = cur
            cur = node

        return pre
    # 链表 转 数组，变为 回文数组判断
    def isPalindrome(self, head: [ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #  反转后半部分，总链表长度如果是奇数，cur2比cur1多一个节点
        cur1, cur2 = head, self.reverse_list(slow)

        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True

    # 链表 转 数组，变为 回文数组判断
    # def isPalindrome(self, head: [ListNode]) -> bool:
    #     list_ = []
    #     cur = head
    #     len_ = 0
    #     while cur:
    #         list_.append(cur.val)
    #         len_ += 1
    #         cur = cur.next
    #     for i in range(0, len_ // 2):
    #         if list_[i] != list_[len_ - i - 1]:
    #             return False
    #     return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

s = Solution()
print(s.isPalindrome(head))