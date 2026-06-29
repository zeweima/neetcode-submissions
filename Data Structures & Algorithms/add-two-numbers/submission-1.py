# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        carry_over = 0
        tail = dummy
        while l1 and l2:
            NewNode = ListNode(
                val = (l1.val+l2.val + carry_over)%10
            )
            carry_over = (l1.val+l2.val + carry_over)//10
            tail.next = NewNode
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            tmp = l1
        else:
            tmp = l2

        while tmp:
            NewNode = ListNode(
                val = (tmp.val + carry_over)%10
            )
            carry_over = (tmp.val + carry_over)//10
            tail.next = NewNode
            tail = tail.next
            tmp=tmp.next
        if carry_over:
            NewNode = ListNode(
                val = 1
            )
            carry_over = 0
            tail.next = NewNode
        return dummy.next