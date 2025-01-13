"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network 
where connections[i] = [ai, bi] represents a connection between computers ai and bi. 
Any computer can reach any other computer directly or indirectly through the network.
You are given an initial computer network connections. 
You can extract certain cables between two directly connected computers, 
and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. 
If it is not possible, return -1.

Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 
Constraints:
1 <= n <= 10**5
1 <= connections.length <= min(n * (n - 1) / 2, 10**5)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
"""
class Solution:
    def dfs(self, network, visited, com):
        visited[com] = True
        for connected_com in network[com]:
            if not visited[connected_com]:
                self.dfs(network, visited, connected_com)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1

        network = [[] for i in range(n)]

        for connection in connections:
            network[connection[0]].append(connection[1])
            network[connection[1]].append(connection[0])

        visited = [False]*n
        op = 0
        for computer in range(n):
            if not visited[computer]:
                # visit all connected com
                self.dfs(network, visited, computer)
                op += 1

        return op-1
        
