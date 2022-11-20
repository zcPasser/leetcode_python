#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py83_RemovesDuplicateElementsFromSortedLinkedLists.py
# @Time      :2022/2/20 16:45
# @Author    :zhangcai

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        slow, fast = head, head.next

        while fast != None:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next

        if slow.next != None:
            slow.next = None
        return head

def main():
    head = ListNode(1)
    p = head
    data = [1, 1, 2]
    len_data = len(data)
    for i in range(1, len_data):
        p.next = ListNode(data[i])
        p = p.next

    s = Solution()
    print(s.deleteDuplicates(head))
    return


if __name__ == "__main__":
    main()