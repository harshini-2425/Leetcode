class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        mob = 0
        prefix = 0
        mp = {0:1}
        c = 0
        for i in range(len(nums)):
            prefix += nums[i]
            mob = prefix%k
            if mob < 0:
                mob += k
            if mob in mp:
                c += mp[mob]
                mp[mob] += 1
            else:
                mp[mob] = 1
        return c