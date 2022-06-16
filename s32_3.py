# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, que = [], collections.deque()
        que.append(root)
        while que:
            temp =collections.deque()
            for i in range(len(que)):
                #永远只能从左边出值，否则深度可能不对
                node =que.popleft()
                if len(res)%2 : temp.appendleft(node.val) 
                else: temp.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(list(temp)) #注意这里把双端队列temp变成list
        return res
