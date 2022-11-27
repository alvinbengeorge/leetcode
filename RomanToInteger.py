class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        output = 0
        previous = None
        for ch in s.upper():
            if previous and values[previous] >= values[ch]:
                previous = None
            output += values[ch] - (2*values[previous] if previous else 0)

            previous = ch
        return output


        
