# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def recur(node, high):
            nonlocal count

            if not node:
                return
            if node.val >= high:
                count+=1
                high = node.val

            recur(node.left, high)           
            recur(node.right, high) 
        
        recur(root, root.val)
        
        return count