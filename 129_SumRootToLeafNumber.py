# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def func(root, nombre):
            result = nombre*10 + root.val
            if root.left != None and root.right != None:
                return func(root.left, result) + func(root.right, result)
            elif root.left != None:
                return func(root.left, result)
            elif root.right != None:
                return func(root.right, result)
            else:
                return result
            
            return somme1 + somme2
        

        return func(root, 0)