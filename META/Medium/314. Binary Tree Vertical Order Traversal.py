"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col = defaultdict(list)
        queue = deque([(root, 0)])
        result = []
        # BFS (Breadth-First Search)
        # T(n) = O(n) BFS
        # S(n) = O(n) max(col) = n, max(queue) = n
        while queue:
            node, x = queue.popleft()
            col[x].append(node.val)
            # print(x, node.val)
            if node.left:
                queue.append((node.left, x-1))
            if node.right:
                queue.append((node.right, x+1))
        
        return [col[x] for x in range(min(col), max(col)+1)]
