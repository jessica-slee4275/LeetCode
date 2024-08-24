"""
There is an undirected graph consisting of n nodes numbered from 1 to n. 
You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.
You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return true if it is possible to make the degree of each node in the graph even, otherwise return false.
The degree of a node is the number of edges connected to it.

Example 1:
Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
Output: true
Explanation: The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.

Example 2:
Input: n = 4, edges = [[1,2],[3,4]]
Output: true
Explanation: The above diagram shows a valid way of adding two edges.

Example 3:
Input: n = 4, edges = [[1,2],[1,3],[1,4]]
Output: false
Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
 

Constraints:
3 <= n <= 10**5
2 <= edges.length <= 10**5
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There are no repeated edges.
"""
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        G = defaultdict(list)
        G_cnt = defaultdict(int)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
            G_cnt[i] += 1
            G_cnt[j] += 1

        odds = []
        for node, degree in G_cnt.items():
            if degree % 2 == 1:
                odds.append(node)
        # print('odds', odds)
        if len(odds) == 0:
            return True
        
        if len(odds) == 2:
            a, b = odds[0], odds[1]
            if a not in G[b]: return True
            for node in range(1, n+1):
                if a not in G[node] and b not in G[node]:
                    return True

        if len(odds) == 4:
            a, b, c, d = odds[0], odds[1], odds[2], odds[3]
            if a not in G[b] and c not in G[d]: return True
            if a not in G[c] and b not in G[d]: return True
            if a not in G[d] and b not in G[c]: return True
        return False
