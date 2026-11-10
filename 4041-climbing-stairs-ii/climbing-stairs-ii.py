class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for j in range(1, n + 1):

            for jump in range(1, 4):

                i = j - jump

                if i >= 0:
                    total = dp[i] + costs[j - 1] + jump * jump

                    dp[j] = min(dp[j], total)

        return dp[n]
        