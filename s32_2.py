# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #DFS
        if not root: return []
        res, que =[], collections.deque()
        que.append(root)
        while que:
            temp =[]
            for i in range(len(que)):
                node = que.popleft()
                temp.append(node.val)
                if node.left: 
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(temp)
        return res
