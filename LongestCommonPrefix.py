class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = min(map(len, strs))
        output = ""
        for i in range(minLength):
            if not all([j.startswith(output + strs[0][i]) for j in strs]):
                break
            else:
                output += strs[0][i]
        return output

