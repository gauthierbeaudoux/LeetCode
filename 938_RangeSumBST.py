# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        L = [root]
        while len(L) > 0 :
            x = L[0]
            L.pop(0)
            if x.val <= high and x.val >= low:
                result += x.val
            if x.left != None:
                L.append(x.left)
            if x.right != None:
                L.append(x.right)
        return result