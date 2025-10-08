# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p_n, q_n):
            if (not p_n and q_n) or (p_n and not q_n):
                return False
            if not p_n and not q_n:
                return True
            if p_n.val != q_n.val:
                return False
            left = same(p_n.left, q_n.left)
            right = same(p_n.right, q_n.right)
            return left and right
        return same(p, q)
