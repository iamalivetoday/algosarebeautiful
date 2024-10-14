# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # If any elements remain in list1 or list2, append them
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Return the merged list starting at dummy.next
        return dummy.next
