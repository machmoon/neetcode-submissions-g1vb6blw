# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        # print(slow.next.val)
        while curr:
            # [None<-6<-8]
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # left = head
        right = prev
        left = head

        while right:
            print(left.val)
            temp = left.next
            temp2 = right.next
            left.next = right
            # print(1)
            # print(left.val)
            left.next.next = temp
            
            right = temp2
            # print(2)
            # print(left.val, right.val)
            left = temp