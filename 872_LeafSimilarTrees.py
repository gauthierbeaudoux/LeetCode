# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def liste_node(L, root):
            if root == None:
                return L
            if root.left == None and root.right == None:
                return L.append(root.val)
            return liste_node(L, root.left), liste_node(L, root.right)
        L1 = []
        L2 = []
        liste_node(L1, root1)
        liste_node(L2, root2)
        if L1 == L2:
            return True
        return False
