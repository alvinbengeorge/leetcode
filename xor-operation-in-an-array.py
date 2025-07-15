class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xorValue = 0
        for i in range(start, start + 2 * n, 2):
            xorValue ^= i
        return xorValue
