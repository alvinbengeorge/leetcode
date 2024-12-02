class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = ""
        stack = ""
        scanned = ""
        for i in s:            
            if i == "(":
                stack += "("
            else:
                stack = stack[:-1]
            scanned += i
            if stack == "":
                output += scanned[1:-1]
                scanned = ""
            print("stack: ", stack)
            print("scanned: ", scanned)
            print()
        return output
                
