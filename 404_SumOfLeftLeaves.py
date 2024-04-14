# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def new_func(root, is_left):
            if root.right == None and root.left == None:
                if is_left:
                    return root.val
                else:
                    return 0
            elif root.right == None:
                return new_func(root.left, True)
            elif root.left == None:
                return new_func(root.right, False)
            else:
                return new_func(root.right, False) + new_func(root.left, True)

    
        return new_func(root, False)