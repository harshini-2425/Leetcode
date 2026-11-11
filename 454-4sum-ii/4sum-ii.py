class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        freq_sum = {}

        for a in nums1:
            for b in nums2:
                pair_sum = a + b
                freq_sum[pair_sum] = freq_sum.get(pair_sum,0)+1

        cnt = 0

        for c in nums3:
            for d in nums4:
                n = -(c + d)
                cnt+= freq_sum.get(n,0)
        return cnt