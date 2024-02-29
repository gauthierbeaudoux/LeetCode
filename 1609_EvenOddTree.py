# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        nb_par_couche = {}
        
        def verification(root, couche):
            if couche % 2 == 0 and root.val % 2 == 0:
                return False
            elif couche % 2 == 1 and root.val % 2 == 1:
                return False
            
            if couche in nb_par_couche.keys():
                nb_par_couche[couche].append(root.val)
            else:
                nb_par_couche[couche] = [root.val]
               
            verif_droit = True
            verif_gauche = True
            if root.left is not None:
                verif_gauche = verification(root.left, couche+1)
            if root.right is not None:
                verif_droit = verification(root.right, couche+1)
            
            if root.left is None and root.right is None:
                return True
            return verif_droit and verif_gauche
            
            
             
             
        def is_sorted(liste, strict_croissant=True):
            if strict_croissant:
                for i in range(len(liste)-1):
                    if liste[i] >= liste[i+1]:
                        return False
                return True
            else:
                for i in range(len(liste)-1):
                    if liste[i] <= liste[i+1]:
                        return False
                return True
        
        if not verification(root, 0):
            return False
        print(nb_par_couche)
        
        for couche, liste in nb_par_couche.items():
            if couche % 2 == 0:
                if not is_sorted(liste):
                    return False
            elif couche % 2 == 1:
                if not is_sorted(liste, False):
                    return False
        return True
            
                