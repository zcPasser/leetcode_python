# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: [ListNode]) -> [ListNode]:
        if head:
            stack = [head]
            p = head.next
            while p:
                if stack:
                    last = stack[-1]
                else:
                    stack.append(p)
                    p = p.next
                    continue
                if p.val > last.val:
                    stack.pop()
                    if stack:
                        stack[-1].next = p
                else:
                    stack.append(p)
                    p = p.next
        return stack[0]

# [5,2,13,3,8]
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

s = Solution()
print(s.removeNodes(head))
