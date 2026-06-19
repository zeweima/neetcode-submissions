# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode
        dummy.next = head 

        leftnode = dummy
        rightnode = dummy
        for _ in range(n):
            rightnode = rightnode.next
        
        while rightnode.next:
            rightnode = rightnode.next
            leftnode = leftnode.next
        
        leftnode.next = leftnode.next.next
        return dummy.next
