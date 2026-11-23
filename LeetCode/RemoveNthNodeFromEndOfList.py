# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        fast = ListNode(0, head)
        while (n > 0):
            fast= fast.next
            n-= 1

        slow = ListNode(0, head)
        while (fast.next):
            slow= slow.next
            fast= fast.next
        
        if (not slow.next.next):
            slow.next= None
        else:
            slow.next= slow.next.next    
        return head

