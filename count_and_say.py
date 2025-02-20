class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def RLE(s):
            res = ""
            c = 1
            prev_e = None
            for e in s:
                if e == prev_e:
                    c += 1
                elif prev_e: 
                    res += str(c) + prev_e
                    c = 1
                prev_e = e
            res += str(c) + e
            # print(res)
            return res
        return RLE(self.countAndSay(n-1))
