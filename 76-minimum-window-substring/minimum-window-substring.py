class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        start = 0
        end = 0
        start_index = 0
        min_len = float('inf')
        cnt = len(t)
        mp = [0]*128
        for i in t:
            mp[ord(i)] += 1
        while end < len(s):
            if mp[ord(s[end])] > 0:
                cnt -= 1
            mp[ord(s[end])] -= 1
            end += 1
            while cnt == 0:
                if end-start < min_len:
                    start_index = start
                    min_len = end-start
                if mp[ord(s[start])] == 0:
                    cnt += 1
                mp[ord(s[start])] += 1
                start +=1
        return "" if min_len == float('inf') else s[start_index:start_index+min_len]

