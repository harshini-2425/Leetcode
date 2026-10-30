import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[node][count] = minimum cost
        # to reach node with consecutive count
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        # Starting node has consecutive count 1
        dist[0][1] = 0

        pq = [(0, 0, 1)]  # cost, node, count

        while pq:
            cost, u, count = heapq.heappop(pq)

            if cost > dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                # Ignore invalid consecutive runs
                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, new_count)
                    )

        return -1
        