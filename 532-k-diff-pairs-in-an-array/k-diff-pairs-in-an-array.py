class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mp = {}
        cnt = 0
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i],0)+1
        for num in mp:
            if k == 0:
                if mp[num] >= 2:
                    cnt += 1
            else:
                if num+k in mp:
                    cnt += 1
        return cnt