# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        revlist =[]
        while head:
            revlist.append(head.val)
            head = head.next
        return revlist[::-1]
        
        """
        :type head: ListNode
        :rtype: List[int]
        """
