class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i] >= 'A' and s[i] <= 'Z':
                st += chr(ord(s[i]) + 32)        
            if s[i] >= 'a' and s[i] <= 'z':
                st += s[i]
            if s[i] >= '0' and s[i] <= '9':
                st += s[i]
        left = 0
        right = len(st)-1
        while left <= right:
            if st[left] == st[right]:
                left += 1
                right -= 1
            else:
                return False
        return True