class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for idx, char in enumerate(s):
            if char == ')' and idx > 0:
                if s[idx-1] == '(':
                    dp[idx] = 2 + dp[idx-2] if idx > 1 else 2
                else:
                    open_location = (idx - 1) - dp[idx-1]
                    if open_location >= 0 and s[open_location] == '(':
                        dp[idx] = 2 + dp[idx-1] + dp[open_location - 1]
        return max(dp) if dp else 0
                        
