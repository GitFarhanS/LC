# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        cache = {val: idx for idx, val in enumerate(inorder)}

        def build_tree(root_index, start, n):
            """
            root_index,
            start,
            n: size of the diction
            """
            if n <= 0:
                return None

            root_val = preorder[root_index]
            inorder_root_index = cache[root_val]
            left_size = inorder_root_index - start


            left = build_tree(
                root_index + 1,
                start,
                left_size
            )
            right = build_tree(
                root_index + left_size + 1,
                inorder_root_index + 1,
                n - left_size - 1
            )

            return TreeNode(root_val, left, right)
        
        return build_tree(0, 0, len(inorder))