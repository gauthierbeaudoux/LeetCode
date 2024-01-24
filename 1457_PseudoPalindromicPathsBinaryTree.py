from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def is_palindrome(list):
            frequence = Counter(list)
            nb_impair = 0
            for value in frequence.values():
                if value % 2 == 1:
                    nb_impair += 1
                if nb_impair > 1:
                    return False
            return True

        def list_palindrome(root, liste):
            liste.append(root.val)
            if root.right == None and root.left == None:
                if is_palindrome(liste):
                    return 1
                else:
                    return 0
            else:
                val_gauche = 0
                val_droite = 0
                if root.left != None:
                    liste_gauche = liste[:]
                    val_gauche = list_palindrome(root.left, liste_gauche)
                if root.right != None:
                    liste_droite = liste[:]
                    val_droite = list_palindrome(root.right, liste_droite)
                return val_gauche + val_droite
        

        liste = []
        return list_palindrome(root, liste)