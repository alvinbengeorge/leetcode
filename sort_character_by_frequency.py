class Solution:
    def getCount(self, s: str) -> dict:
        return {i: s.count(i) for i in set(s)}        
    def frequencySort(self, s: str) -> str:
        return "".join([i*j for j, i in sorted([j[::-1] for j in self.getCount(s).items()], reverse=True)])
        
