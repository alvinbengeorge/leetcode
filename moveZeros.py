def moveZeros(n: int,  a: [int]) -> [int]:
    while 0 in a[:n]:
        a.remove(0)
        a.append(0)
        n-=1
    return a
