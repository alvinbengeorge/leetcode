class Solution:
    def longestPalindrome(self, s: str) -> str:
        isPalindrome = lambda x: x == x[::-1]
        if isPalindrome(s): return s
        for i in range(len(s), 0, -1):
            for j in range(0, len(s)-i+1):
                if isPalindrome(s[j:j+i]): return s[j:j+i]
