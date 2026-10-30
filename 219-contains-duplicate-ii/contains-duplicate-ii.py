class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq = {}
        for i,num in enumerate(nums):
            if num in freq and abs(i-freq[num]) <= k:
                return True
            freq[nums[i]] = i
        return False