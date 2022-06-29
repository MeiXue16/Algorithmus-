# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #链表问题要多考虑双指针
        pre =cur =head
        for i in range(k):
            cur = cur.next
        while cur:
            pre, cur = pre.next, cur.next
        return pre
