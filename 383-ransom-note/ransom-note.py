class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp1 = {}
        for num in magazine:
            mp1[num] = mp1.get(num,0)+1
        for num in ransomNote:
            if num not in mp1 or mp1[num] <= 0:
                return False
            mp1[num] -= 1
        return True
        