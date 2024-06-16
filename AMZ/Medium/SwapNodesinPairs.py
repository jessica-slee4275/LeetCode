"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
 
Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node, return it as is.
        if not head or not head.next:
            return head
        
        # Initialize a dummy node to simplify edge cases, pointing to the head of the list
        dummy = ListNode(-1)
        dummy.next = head
        
        # 'prev_node' starts at the dummy and is used to link to the new pairs
        prev_node = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping logic
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Move 'prev_node' and 'head' to the next pair of nodes
            prev_node = first_node
            head = first_node.next
        
        # The 'next' of the dummy node points to the head of the modified list
        return dummy.next

  
