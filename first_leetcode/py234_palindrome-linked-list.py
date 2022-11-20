# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 用数组存储。
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next
        return vals[::] == vals[::-1]

    # 转为 回文字符串 判断。
    # def isPalindrome(self, head: ListNode) -> bool:
    #     if not head:
    #         return True
    #     linklist_str = []
    #     p = head
    #     while p:
    #         linklist_str += str(p.val)
    #         p = p.next
    #     left, right = 0, len(linklist_str) - 1
    #     while left <= right:
    #         if linklist_str[left] != linklist_str[right]:
    #             return False
    #         left, right = left + 1, right - 1
    #
    #     return True

