"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        val_head = head
        all_map = {None: None}

        while val_head:
            copy = Node(val_head.val)
            all_map[val_head] = copy
            val_head = val_head.next
        
        val_head2 = head
        
        while val_head2:
            copy = all_map[val_head2]
            copy.next = all_map[val_head2.next]
            copy.random = all_map[val_head2.random]
            val_head2 = val_head2.next

        return all_map[head]