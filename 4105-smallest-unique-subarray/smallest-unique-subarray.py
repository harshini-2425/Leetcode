from typing import List
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE = 911382323

        # Build prefix hashes
        prefix1 = [0] * (n + 1)
        prefix2 = [0] * (n + 1)

        for i, num in enumerate(nums):
            prefix1[i + 1] = (prefix1[i] * BASE + num) % MOD1
            prefix2[i + 1] = (prefix2[i] * BASE + num) % MOD2

        def has_unique(length):
            power1 = pow(BASE, length, MOD1)
            power2 = pow(BASE, length, MOD2)

            freq = {}

            for i in range(n - length + 1):
                j = i + length

                h1 = (prefix1[j] - prefix1[i] * power1) % MOD1
                h2 = (prefix2[j] - prefix2[i] * power2) % MOD2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        # Binary search for the minimum valid length
        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if has_unique(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
        