class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        c = 0
        ans = 0
        for num in s:
            if num-1 not in s:
                c = num
                ans = 1
                while (c+1) in s:
                    ans += 1
                    c += 1
                l = max(l,ans)
        return l
        