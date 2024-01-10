# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def create_dic_node(dic, root):
            if root == None or (root.left == None and root.right == None):
                return
            elif root.left == None:
                dic[root.val] = [root.right.val]
                return create_dic_node(dic, root.right)
            elif root.right == None:
                dic[root.val] = [root.left.val]
                return create_dic_node(dic, root.left)
            dic[root.val] = [root.left.val, root.right.val]
            return create_dic_node(dic, root.left), create_dic_node(dic, root.right)

        temps = 0
        dic_node = {}
        create_dic_node(dic_node, root)
        # print(dic_node)

        set_infected = set()
        for key, value in dic_node.items():
            set_infected.add(key)
            for x in value:
                set_infected.add(x)
        # print(set_infected)

        new_infected = [start]
        while len(set_infected) > 0:
            i = 0
            n = len(new_infected)
            while i < n:
                x = new_infected[0]
                set_infected.discard(x)
                if x in dic_node:
                    for value in dic_node[x]:
                        new_infected.append(value)
                        set_infected.discard(value)
                    del dic_node[x]
                list_to_delete = []
                for key, value in dic_node.items():
                    if x in value:
                        new_infected.append(key)
                        set_infected.discard(key)
                        break
                i += 1
                new_infected.pop(0)
            temps += 1
        return temps