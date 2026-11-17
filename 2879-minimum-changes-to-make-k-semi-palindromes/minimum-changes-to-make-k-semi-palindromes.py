class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute the cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                # Try every proper divisor
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    group_len = length // d
                    changes = 0

                    # Check each group for palindrome property
                    for offset in range(d):
                        for t in range(group_len // 2):
                            left = i + offset + t * d
                            right = i + offset + (group_len - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # Step 2: DP
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for parts in range(1, k + 1):

                # Leave at least 2 characters for every remaining part
                max_end = n - 2 * (parts - 1) - 1

                for j in range(i + 1, max_end + 1):
                    if dp[j + 1][parts - 1] != INF:
                        dp[i][parts] = min(
                            dp[i][parts],
                            cost[i][j] + dp[j + 1][parts - 1]
                        )

        return dp[0][k]
        