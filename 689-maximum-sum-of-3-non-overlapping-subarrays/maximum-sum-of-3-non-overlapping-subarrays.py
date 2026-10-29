class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        sums = []
        cur = sum(nums[:k])
        sums.append(cur)
        for i in range(k,n):
            cur += nums[i]-nums[i-k]
            sums.append(cur)
        m = len(sums)
        best = [0]*m
        for i in range(1,m):
            if sums[i] > sums[best[i-1]]:
                best[i] = i
            else:
                best[i] = best[i-1]
        right = [0]*m
        right[m-1] = m-1
        for i in range(m-2,-1,-1):
            if sums[i] >= sums[right[i+1]]:
                right[i] = i
            else:
                right[i] = right[i+1]
        ans = []
        max_total = -1
        for mid in range(k,m-k):
            left = best[mid-k]
            r = right[mid+k]
            total = sums[left]+sums[mid]+sums[r]
            if total > max_total:
                max_total = total
                ans = [left,mid,r]
        return ans

        