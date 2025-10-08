# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        q = collections.deque()
        q.append(root)

        out = []

        while q:
            qLen = len(q)
            temp =[]
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    temp.append(curr.val)
                    q.append(curr.right)
                    q.append(curr.left)
            if temp:
                out.append(temp[0])
        
        return out