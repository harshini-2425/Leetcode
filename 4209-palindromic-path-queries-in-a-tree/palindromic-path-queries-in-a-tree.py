from typing import List
import sys
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        sys.setrecursionlimit(300000)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n

        # Step 1: Find subtree sizes and heavy children
        def dfs(u, p):
            parent[u] = p
            size[u] = 1
            largest = 0

            for v in adj[u]:
                if v == p:
                    continue

                depth[v] = depth[u] + 1
                dfs(v, u)
                size[u] += size[v]

                if size[v] > largest:
                    largest = size[v]
                    heavy[u] = v

        dfs(0, -1)

        # Step 2: Decompose the tree into heavy chains
        head = [0] * n
        pos = [0] * n
        base = [0] * n
        timer = 0

        def decompose(u, h):
            nonlocal timer

            head[u] = h
            pos[u] = timer
            base[timer] = 1 << (ord(s[u]) - ord('a'))
            timer += 1

            if heavy[u] != -1:
                decompose(heavy[u], h)

            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    decompose(v, v)

        decompose(0, 0)

        # Step 3: Segment tree supporting XOR and point updates
        seg = [0] * (2 * n)

        for i in range(n):
            seg[n + i] = base[i]

        for i in range(n - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(p, value):
            p += n
            seg[p] = value
            p //= 2

            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        # XOR over the half-open interval [l, r)
        def range_xor(l, r):
            result = 0
            l += n
            r += n

            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1

                if r & 1:
                    r -= 1
                    result ^= seg[r]

                l //= 2
                r //= 2

            return result

        # Step 4: XOR all characters on the path u -> v
        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v] + 1)
            return result

        # Step 5: Process queries
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                mask = 1 << (ord(c) - ord('a'))
                update(pos[u], mask)

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                # True if at most one bit is set
                answer.append(
                    mask == 0 or (mask & (mask - 1)) == 0
                )

        return answer
        