# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.elements = []
        node = root
        def dfs(node):
            if node == None:
                return 
            if node.val >= L and node.val <=R:
                self.elements.append(node.val)
            if node.val > L:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)
        dfs(node)
        return sum(self.elements)
        
            
        
            
        
            