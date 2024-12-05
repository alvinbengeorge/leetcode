class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i.strip() for i in s.split(' ') if i.strip() != ""][::-1])
