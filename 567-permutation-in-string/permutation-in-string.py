from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        k = len(s1)
        window_count = Counter(s2[:k])
        if s1_count == window_count:
            return True
        for i in range(k,len(s2)):
            window_count[s2[i]] += 1
            left = s2[i-k]
            window_count[left] -= 1
            if window_count[left] == 0:
                del window_count[left]
            if window_count == s1_count:
                return True
        return False