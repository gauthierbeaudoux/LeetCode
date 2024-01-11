# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def max_value(max_node, min_node, root):
            if root == None:
                return
            if max_node == -1:
                global result
                result = -1
            else:
                if abs(root.val-max_node) > result:
                    result = abs(root.val-max_node)
                if abs(root.val-min_node) > result:
                    result = abs(root.val-min_node)
            max_value(max(root.val, max_node), min(root.val, min_node), root.left)
            max_value(max(root.val, max_node), min(root.val, min_node), root.right)
        
        max_value(-1,10**5+1, root)
        return result