#LC 2
#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy_head = ListNode(0) # Create a dummy head to ease list construction
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            total_sum = total_sum % 10

            # Append new node to the list
            current.next = ListNode(total_sum)
            current = current.next

            # Move to the next nodes if available
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return dummy_head.next # Return the next node of dummy head, which is the real start of the list