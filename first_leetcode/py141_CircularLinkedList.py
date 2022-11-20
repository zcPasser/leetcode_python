#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py141_CircularLinkedList.py
# @Time      :2022/2/14 15:39
# @Author    :zhangcai

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False



def main():
    return


if __name__ == "__main__":
    main()