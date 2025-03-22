from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n

        def dfs(node, component_nodes):
            visited[node] = True
            component_nodes.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component_nodes)

        def is_complete(component_nodes):
            size = len(component_nodes)
            edge_count = 0
            for node in component_nodes:
                edge_count += len(graph[node])
            return edge_count == size * (size - 1)

        complete_count = 0

        for i in range(n):
            if not visited[i]:
                component_nodes = []
                dfs(i, component_nodes)
                if is_complete(component_nodes):
                    complete_count += 1

        return complete_count

print(Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))  # Output: 3
