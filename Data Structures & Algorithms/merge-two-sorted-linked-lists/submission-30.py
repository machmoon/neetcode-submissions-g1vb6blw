# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, list1: Optional[ListNode]):
        result = []
        while list1 != None:
            result.append(list1.val)
            list1 = list1.next
        print(result)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = list1
        prev1 = dummy

        # list1 = [1,2,4], list2 = [5]
        # [None-> 1-> 1, 2, 4]
        # temp == 3

        while list1 and list2:
            print("list 1")
            self.printList(list1)
            print("list 2")
            self.printList(list2)
            print("list")
            self.printList(dummy.next)
            # while list2 and list1.val >= list2.val:
            
            
            if list1.val < list2.val:
                prev1 = list1
                list1 = list1.next
            else: 
                temp = list2.next
                list2.next = list1
                prev1.next = list2
                prev1 = list2
                
                list2 = temp

        if list2:
            prev1.next = list2
        if list1:
            prev1.next = list1


        return dummy.next