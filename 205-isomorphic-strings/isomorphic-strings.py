class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp1 = {}
        mp2= {}
        for i,j in zip(s,t):
            if i in mp1 and mp1[i] != j:
                return False
            if j in mp2 and mp2[j] != i:
                return False
            mp1[i] = j
            mp2[j] = i
        return True 

