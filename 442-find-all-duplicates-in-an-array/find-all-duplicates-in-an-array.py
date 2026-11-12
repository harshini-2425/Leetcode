class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq = {}
        res= []
        for num in nums:
            freq[num] = freq.get(num,0)+1
            if freq[num] >= 2:
                res.append(num)
        return res
        