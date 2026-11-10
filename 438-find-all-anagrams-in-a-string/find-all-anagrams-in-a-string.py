class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        scount = [0]*26
        pcount = [0]*26
        res = []
        for i in range(len(p)):
            pcount[ord(p[i]) - ord("a")] += 1
        for i in range(len(s)):
            scount[ord(s[i])-ord("a")] += 1
            if i >= len(p):
                scount[ord(s[i-len(p)])-ord("a")] -= 1
            if scount == pcount:
                res.append(i-len(p)+1)
        return res