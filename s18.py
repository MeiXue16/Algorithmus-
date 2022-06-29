# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre =head
        cur =head.next
        if head.val== val: return cur  #一般来说.val出现在判断和循环条件中。这里如果不加 .val，就无法执行这句
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        if cur: pre.next = cur.next
        return head
