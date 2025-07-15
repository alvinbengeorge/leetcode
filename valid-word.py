class Solution:
    def isValid(self, word: str) -> bool:
        base_conditions = all([
            len(word) >= 3,            
            word.isalnum(),
            any([i in word.lower() for i in ['a','e','i','o','u']]),
            any([i in word.lower() for i in ({chr(i) for i in range(97, 123)} - {'a','e','i','o','u'})])
            
        ])
        return base_conditions
