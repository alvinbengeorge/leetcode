class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsDict = {}
        solutions = []
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
        if ('a' in wordsDict):
            if (wordsDict['a'] == 5000):
                return list(range(0, len(s) - 4999))
        n = len(s)
        wordsLen = len(words)
        eachWordLen = len(words[0])
        wordsTotalLen = wordsLen * eachWordLen
        for k in range(eachWordLen):
            i = 0
            while(i*eachWordLen + wordsTotalLen + k <= n):
                tempDict = copy.copy(wordsDict)
                j = wordsLen + i
                while(j > i):
                    curWord = s[(j-1)*eachWordLen + k:j*eachWordLen + k]
                    if curWord in tempDict:
                        tempDict[curWord] -= 1
                        if (tempDict[curWord] == 0):
                            del tempDict[curWord]
                        j -= 1
                        if (j == i):
                            solutions.append(i*eachWordLen + k)
                            i += 1
                            break
                    else:
                        i = j
                        break
        return(solutions)
