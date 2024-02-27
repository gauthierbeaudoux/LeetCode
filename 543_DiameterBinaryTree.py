root = [1,2,3,4,5]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def cout_uni(root):
            cout_droit = 0
            cout_gauche = 0
            if root.left is not None:
                cout_gauche = 1+cout_uni(root.left)
            if root.right is not None:
                cout_droit = 1+cout_uni(root.right)
            
            return max(cout_droit, cout_gauche)
        
        def cout_final(root):
            if root.left is None and root.right is None:
                return 0
            if root.right is None:
                return 1+cout_uni(root.left)
            if root.left is None:
                return 1+cout_uni(root.right)

            return max(cout_final(root.left), cout_final(root.right),
                       cout_uni(root.left) + cout_uni(root.right) + 2)
            
        return cout_final(root)