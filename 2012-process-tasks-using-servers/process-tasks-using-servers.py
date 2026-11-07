import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []

        # Initially, all servers are available
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i in range(len(tasks)):

            time = max(time, i)

            # Release all servers that have completed their tasks
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:
                time = busy[0][0]

                # Release all servers available at this time
                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Assign the task to this server
            free_time = time + tasks[i]

            heapq.heappush(busy, (free_time, weight, index))

        return ans
        