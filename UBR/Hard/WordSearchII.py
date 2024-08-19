"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 
Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 
Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10**4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, root):
            w = board[x][y]
            cur = root[w]
            word = cur.pop('#', False)
            print(root, x, y, w, word)
            if word:
                res.append(word)
            board[x][y] = '*' # visited

            for dirX, dirY in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curX, curY = x + dirX, y + dirY
                if 0 <= curX < m and 0 <= curY < n and board[curX][curY] in cur:
                    dfs(curX, curY, cur)
            board[x][y] = w
            if not cur:
                root.pop(w)
            
        trie = {}
        # trie data structure 
        """
        {'o': {'a': {'t': {'h': {'#': 'oath'}}}}, 'p': {'e': {'a': {'#': 'pea'}}}, 
        'e': {'a': {'t': {'#': 'eat'}}}, 'r': {'a': {'i': {'n': {'#': 'rain'}}}}}
        """
        for word in words:
            cur = trie
            for w in word:
                cur = cur.setdefault(w, {})
            cur['#'] = word
        m, n = len(board), len(board[0])
        
        res = []

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res
