class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = 0
        a, b = [int(i) for i in a], [int(i) for i in b]
        l1, l2 = len(a), len(b)
        if l1 > l2:
            b = [0 for i in range(l1 - l2)] + b
            max_len = l1
        else:
            a = [0 for i in range(l2 - l1)] + a
            max_len = l2
        for i in range(max_len - 1, -1, -1):
            a[i] = a[i] + b[i]
            if a[i] >= 2:                
                a[i] -= 2
                if i == 0:
                    a = [1] + a
                else:
                    a[i-1] += 1
        return "".join([str(i) for i in a])
            
        
