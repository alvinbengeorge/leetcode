class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    j = -1
    lastSeen = {}

    for i, c in enumerate(s):
      j = max(j, lastSeen.get(c, -1))
      ans = max(ans, i - j)
      lastSeen[c] = i

    return ans
