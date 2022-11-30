class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        reverseBrackets = {v: k for k, v in brackets.items()}
        stack = ""
        if any([s.startswith(i) for i in brackets]): return False
        for i in s:
            if i not in brackets:
                stack += i 
            else:
                if (len(stack) == 0 and i in ['}', ']', ')']) or stack[-1] != brackets[i]: 
                    return False
                else: stack = stack[:-1]
        return not stack
            
