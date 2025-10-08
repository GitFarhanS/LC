# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        num2 = dummy
        carry = 0

        while l1 or l2:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            carry = num // 10
            num2.next = ListNode(num % 10)
            num2 = num2.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            num2.next = ListNode(carry)
        
        return dummy.next
