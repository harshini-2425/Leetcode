from collections import defaultdict
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        # Store (query_time, original_index)
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        freq = defaultdict(int)

        left = 0
        right = 0
        active = 0

        ans = [0] * len(queries)

        for q, idx in sorted_queries:

            # Add logs with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
        