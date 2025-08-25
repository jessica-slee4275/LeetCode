"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities 
(this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 
Constraints:
2 <= n <= 5 * 10**4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # sign == 1 : original edge u -> v (away from 0, needs flip when traversed from 0 side)
        # sign == 0 : original edge v -> u (toward 0, no flip needed)
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = [False]*n

        def dfs(u: int) -> int:
            visited[u] = True
            need = 0
            for v, sign in graph[u]:
                if not visited[v]:
                    need += sign + dfs(v)
            return need

        return dfs(0)

        # graph = defaultdict(list)
        # for u, v in connections:
        #     graph[u].append((v, 1))
        #     graph[v].append((u, 0))

        # visited = [False]*n
        # flips = 0

        # q = deque([0])
        # visited[0] = True

        # while q:
        #     cur = q.popleft()
        #     for nxt, sign in graph[cur]:
        #         if visited[nxt]: continue
        #         flips += sign
        #         visited[nxt] = True
        #         q.append(nxt)
        # return flips
