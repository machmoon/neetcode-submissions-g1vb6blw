# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        curr = result
        carry = 0

        while l1 or l2 or carry:
        
            if not l1: 
                first = 0
            else:
                first = l1.val
            if not l2: 
                second = 0
            else:
                second = l2.val
            val = first + second + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return result.next