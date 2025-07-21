class Solution:
    def makeFancyString(self, s: str) -> str:
        consecutives = [s[0]]
        for i in s[1:]:
            if consecutives[-1][0] == i:
                consecutives[-1] += i
            else:
                consecutives.append(i)
        return "".join([i[:2] for i in consecutives])
