class Solution:
    def getLucky(self, s: str, k: int) -> int:
        output = "".join([str(ord(i) - 96) for i in s.lower()])
        for i in range(k):
            output = str(sum([int(n) for n in output]))
        return int(output)
        
