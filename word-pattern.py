from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        frequency_set = {}
        s = s.split(' ')
        if len(pattern) != len(s): return False
        for count, i in enumerate(pattern):
            if i not in frequency_set:
                frequency_set[i] = s[count]
            elif frequency_set[i] != s[count]:
                return False
        values = frequency_set.values()
        if any([list(values).count(i) > 1 for i in values]):
            return False
        return True
        
