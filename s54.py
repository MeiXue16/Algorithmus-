# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# methode 1
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root): #定义倒序的序列。中序遍历（左根右）结果为递增序列，因此倒着就是倒序的：右根左
            if (not root) or self.k==0: return
            dfs(root.right)
            self.k -= 1
            if self.k ==0:
                self.res = root.val
                return
            dfs(root.left)
        
        self.k = k
        dfs(root)
        return self.res

# methode 2
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
