# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if (head):   
            fast = head
            slow = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            second = slow.next
            slow.next = None

            prev = None
            slow.next= None
            while second:
                nxt = second.next
                second.next = prev
                prev = second
                second = nxt

            second = prev
            first = head

            while second:
                temp1 = first.next
                temp2 = second.next

                first.next = second
                second.next = temp1

                first = temp1
                second = temp2