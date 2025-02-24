from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs1(node: int, parent: int, time: int) -> bool:
            if node == 0:
                ts[node] = min(ts[node], time)
                return True
            for neighbor in graph[node]:
                if neighbor != parent and dfs1(neighbor, node, time + 1):
                    ts[neighbor] = min(ts[neighbor], time + 1)
                    return True
            return False

        def dfs2(node: int, parent: int, time: int, profit: int):
            if time == ts[node]:
                profit += amount[node] // 2
            elif time < ts[node]:
                profit += amount[node]
            nonlocal max_profit
            if len(graph[node]) == 1 and graph[node][0] == parent:
                max_profit = max(max_profit, profit)
                return
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs2(neighbor, node, time + 1, profit)

        n = len(edges) + 1
        graph = defaultdict(list)
        ts = [n] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs1(bob, -1, 0)
        ts[bob] = 0
        max_profit = -inf
        dfs2(0, -1, 0, 0)
        return max_profit

edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [0, 2, 3, 4, 5]
solution = Solution()
print(solution.mostProfitablePath(edges, bob, amount))  # 6