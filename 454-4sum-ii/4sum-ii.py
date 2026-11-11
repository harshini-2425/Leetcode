class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        pair_sum_freq = {}

        for a in nums1:
            for b in nums2:
                pair_sum = a + b
                pair_sum_freq[pair_sum] = pair_sum_freq.get(pair_sum,0)+1

        count = 0

        for c in nums3:
            for d in nums4:
                needed = -(c + d)
                count+= pair_sum_freq.get(needed,0)

        return count