# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#iteration method

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    
#Rekursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #rekursion
        def reklist(pre, cur):
            if not cur:
                return pre               #终止条件
            rev = reklist(cur, cur.next) #按顺序递归链表
            cur.next = pre               #重新分配指针，准备开始逆序
            return rev                   #逆序链表
        return reklist(None, head)

