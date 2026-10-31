class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        res = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                continue
            res.append(nums1[i])
        st = set(res)
        return list(st)