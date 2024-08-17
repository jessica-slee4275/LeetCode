"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
  3
 / \
 1 4
  \
   2
   
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
    5
   / \
  3   6
 / \
 2  4
/
1
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10**4
0 <= Node.val <= 10**4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.setList(root, values)
        return sorted(values)[k-1]
    def setList(self, root, values):
        if root is None:
            return
        # print(root.val)
        values.append(root.val)
        self.setList(root.left, values)
        self.setList(root.right, values)
