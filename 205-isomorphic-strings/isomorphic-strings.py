class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl = [0]*200
        tl = [0]*200
        for i in range(len(s)):
            if sl[ord(s[i])] != tl[ord(t[i])]:
                return False
            sl[ord(s[i])] = i+1
            tl[ord(t[i])] = i+1
        return True

