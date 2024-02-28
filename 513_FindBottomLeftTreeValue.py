# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def leftmost(root, couche):
            if root.left is None and root.right is None:
                return couche, root.val
            if root.left is not None and root.right is not None:
                profondeur_gauche, valeur_gauche = leftmost(root.left, couche+1)
                profondeur_droit, valeur_droit = leftmost(root.right, couche+1)
                if profondeur_gauche >= profondeur_droit:
                    return profondeur_gauche, valeur_gauche
                else:
                    return profondeur_droit, valeur_droit
            if root.left is not None:
                return leftmost(root.left, couche+1)
            if root.right is not None:
                return leftmost(root.right, couche+1)
                
            
            
        return leftmost(root, 0)[1]