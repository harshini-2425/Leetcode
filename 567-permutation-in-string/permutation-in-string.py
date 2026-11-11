from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        matches = 0
        d1, d2 = [0]*26, [0]*26
        for i in range(len(s1)):
            d1[ord(s1[i])-ord('a')]+=1
            d2[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            if d1[i] == d2[i]:
                matches += 1
        if matches == 26:
            return True
        l=0
        for r in range(len(s1), len(s2)):
            index = ord(s2[r])-ord('a')
            d2[index]+=1
            if d1[index]==d2[index]:
                matches +=1
            elif d1[index]+1==d2[index]:
                matches -=1
            
            index = ord(s2[l])-ord('a')
            d2[index]-=1
            if d1[index]==d2[index]:
                matches +=1
            elif d1[index]-1==d2[index]:
                matches -=1
            l+=1
            
            if matches == 26:
                return True
        return False
