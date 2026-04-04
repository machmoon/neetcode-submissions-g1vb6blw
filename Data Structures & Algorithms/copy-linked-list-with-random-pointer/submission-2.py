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
        
        oldNodetoNewDeepCopy = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            oldNodetoNewDeepCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldNodetoNewDeepCopy[curr]
            copy.next = oldNodetoNewDeepCopy[curr.next]
            copy.random = oldNodetoNewDeepCopy[curr.random]
            curr = curr.next
        
        return oldNodetoNewDeepCopy[head]