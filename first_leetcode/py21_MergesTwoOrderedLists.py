#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py21_MergesTwoOrderedLists.py
# @Time      :2022/2/16 16:18
# @Author    :zhangcai

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists2(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            small = list1
            big = list2
        else:
            small = list2
            big = list1
        head = last = small
        while big is not None and small is not None:
            if small.val <= big.val:
                last = small
                small = small.next
            else:
                last.next = big
                last = big
                small, big = big, small

        if small is None and big is not None:
            last.next = big
        return head

def main():
    return


if __name__ == "__main__":
    main()