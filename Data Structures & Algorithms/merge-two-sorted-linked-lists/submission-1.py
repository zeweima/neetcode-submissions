# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # merge_dummy = ListNode()
        # tail = merge_dummy
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         list1_next = list1.next
                
        #         tail.next = list1
        #         tail = tail.next
        #         tail.next = None
                
        #         list1 = list1_next
        #     else:
        #         list2_next = list2.next
                
        #         tail.next = list2
        #         tail = tail.next
        #         tail.next = None
                
        #         list2 = list2_next
        # if list1:
        #     tail.next = list1
        # if list2:
        #     tail.next = list2
        # return merge_dummy.next
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val<=list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

