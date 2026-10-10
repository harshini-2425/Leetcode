class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        startvalue = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        mini = min(nums)
        start = max(1,1-mini)
        return start        