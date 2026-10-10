class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        startvalue = 0
        pre = [0]*len(nums)
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] += pre[i-1]+nums[i]
        m = min(pre)
        start = max(1,1-m)
        return start        