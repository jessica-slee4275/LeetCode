"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(left, right, prefix): # depth first search
            if len(prefix) == n*2: # pair of '()'
                res.append(prefix)
            if left < n:
                print(left, right, prefix)
                # recursive 2 0 ((
                dfs(left+1, right, prefix + '(')
                
            if right < left:
                # print(left, right, prefix)
                dfs(left, right+1, prefix + ')')
                
        dfs(0, 0, '')
        
        return res
