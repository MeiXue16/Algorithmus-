"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#method 1
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None  #也可以直接写return.
        #建立哈希表，先复制每个节点的值
        dic= {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        #构建节点的next和random指向
        cur = head
        while cur:
            dic[cur].next =dic.get(cur.next)  #get(**)是用来调取键**对应的值
            dic[cur].random = dic.get(cur.random)
            cur =cur.next
        return dic[head]
      
      
  #method 2
  class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return deepcopy(head) #深拷贝
