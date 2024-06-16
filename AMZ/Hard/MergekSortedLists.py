"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10**4
0 <= lists[i].length <= 500
-10**4 <= lists[i][j] <= 10**4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10**4.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def merge(self, left: ListNode, right: ListNode) -> ListNode:
    #     dummy = ListNode(-1)
    #     temp = dummy
    #     while left and right:
    #         # add val to dummy and remove val from left/right
    #         if left.val < right.val:
    #             temp.next = left
    #             temp = temp.next
    #             left = left.next
    #         else:
    #             temp.next = right
    #             temp = temp.next
    #             right = right.next
    #     while left:
    #         temp.next = left
    #         temp = temp.next
    #         left = left.next
    #     while right:
    #         temp.next = right
    #         temp = temp.next
    #         right = right.next
    #     print('dummy', dummy)
    #     return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1 : return lists[0]
        # res = None
        # for i in range(len(lists)//2):
        #     res = self.merge(lists[i], lists[i+1])
        # if len(lists)%2 != 0:
        #    res = self.merge(lists[len(lists)-2], lists[len(lists)-1])     
        # return res

        m = len(lists) // 2

        l1 = self.mergeKLists(lists[:m])
        l2 = self.mergeKLists(lists[m:])

        dummy = ListNode(-1)
        cur = dummy

        while(l1 and l2):
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return dummy.next
