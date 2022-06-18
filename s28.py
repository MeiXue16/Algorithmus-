# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        #定义递归函数：1. 同时越过所有节点，说明相等，返回true
        #             2. 一个左节点/右节点已经遍历完了，另一个没有，或者两者不等，返回 false
        #             3. 循环返回（l.left，r.right）以及(l.right, r.left)
        def rekur(leftnode , rightnode): 
            if not leftnode and not rightnode: return True
            if not leftnode or not rightnode or leftnode.val != rightnode.val:  return False
            return rekur(leftnode.left , rightnode.right) and rekur(leftnode.right , rightnode.left)
        return  rekur(root.left, root.right)
