class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        freq = [0] * 100001
        for d in diff:
            freq[d] += 1

        for d in range(100000, 0, -1):
            if k <= 0:
                break

            use = min(k, freq[d])
            freq[d] -= use
            freq[d - 1] += use
            k -= use

        return sum(d * d * count for d, count in enumerate(freq))