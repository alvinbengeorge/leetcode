class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = 0
        for i in range(len(digits)):
            d += digits[i] * (10 ** (len(digits) - i - 1))
        d += 1
        return [int(i) for i in str(d)]
