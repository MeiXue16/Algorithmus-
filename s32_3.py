# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, que =[], collections.deque([root])
        while que:
            temp =collections.deque()
            for i in range(len(que)):
                node = que.popleft()
                if len(res) % 2 : temp.appendleft(node.val)
                else: temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(list(temp))
        return res
