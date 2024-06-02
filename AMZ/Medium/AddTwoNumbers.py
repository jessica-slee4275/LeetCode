"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multi = 1
        l1_sum = 0
        l2_sum = 0
        while(l1):
            l1_sum += l1.val*(multi)
            multi *= 10
            l1 = l1.next
        multi = 1
        while(l2):
            l2_sum += l2.val*(multi)
            multi *= 10
            l2 = l2.next

        dummy = ListNode()  
        current = dummy 
        for num in list(str(l1_sum + l2_sum))[::-1]:
            current.next = ListNode(int(num)) 
            current = current.next 
        return dummy.next
