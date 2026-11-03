class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if target - nums[i] in freq:
                return [freq[target-nums[i]],i]
            freq[nums[i]] = i
        
        