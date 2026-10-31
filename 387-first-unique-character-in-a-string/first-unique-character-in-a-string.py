class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq= [0]*26    
        for i in range(len(s)):
            freq[ord(s[i]) - ord("a")] += 1
        for i,char in enumerate(s):
            if freq[ord(char)-ord("a")] == 1:
                return i
        return -1

    

        