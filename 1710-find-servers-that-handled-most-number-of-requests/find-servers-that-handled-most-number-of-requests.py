import heapq
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially, all servers are available
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # Update server availability
        def update(pos, value):
            idx = size + pos
            tree[idx] = value

            idx //= 2

            while idx:
                tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
                idx //= 2

        # Find the first available server with index >= start
        def find_first(node, left, right, start):

            if right < start or tree[node] == 0:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            res = find_first(2 * node, left, mid, start)

            if res != -1:
                return res

            return find_first(2 * node + 1, mid + 1, right, start)

        # Busy servers: (finish_time, server_id)
        busy = []

        # Number of requests handled by each server
        count = [0] * k

        for i in range(len(arrival)):

            current_time = arrival[i]

            # Release servers that have finished their requests
            while busy and busy[0][0] <= current_time:
                finish_time, server = heapq.heappop(busy)
                update(server, 1)

            # Starting server index
            start = i % k

            # Find next available server
            server = find_first(1, 0, size - 1, start)

            # Wrap around if necessary
            if server == -1:
                server = find_first(1, 0, size - 1, 0)

            # All servers are busy: drop the request
            if server == -1:
                continue

            # Assign request
            update(server, 0)

            count[server] += 1

            finish_time = current_time + load[i]

            heapq.heappush(busy, (finish_time, server))

        # Find servers handling the maximum number of requests
        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
        