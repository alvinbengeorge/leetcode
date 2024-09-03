class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join([i for i in s.lower() if i.isalnum()])).strip()
        return s[::-1] == s
        
