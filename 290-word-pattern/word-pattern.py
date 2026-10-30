class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = list(s.split())
        if len(ls) != len(pattern):
            return False
        indexp = {}
        indexs = {}
        for a,b in zip(pattern,ls):
            if a in indexp and indexp[a] != b:
                return False
            if b in indexs and indexs[b] != a:
                return False
            indexp[a] = b
            indexs[b] = a
        return True