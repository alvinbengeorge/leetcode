class Solution:
    def getCount(self, s: str) -> dict:
        return {i: s.count(i) for i in set(s)}
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getCount(s) == self.getCount(t)
        
