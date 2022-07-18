# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #双指针，当指针都指向公共节点时返回，如果全链表遍历完成则返回空值
        a, b =headA, headB
        while a!=b:
            a =a.next if a else headB
            b =b.next if b else headA
        return a
