class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxCount = 0
        for i in s:
            if i=="(":
                stack.append("(")
            if i==")":
                stack.pop()
            if (len(stack) > maxCount):
                maxCount = len(stack)
        return maxCount
        
