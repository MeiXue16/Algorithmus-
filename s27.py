# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root : return 
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left) #parallel zuordung
        return root

#method 2     
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root : return 
        temp =root.left
        root.left= self.mirrorTree(root.right)  
        root.right= self.mirrorTree(temp)
        return root
