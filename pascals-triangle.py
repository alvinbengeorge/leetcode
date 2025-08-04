class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            triangle.append([1])
            for j in range(1, i):
                triangle[-1].append(triangle[-2][j] + triangle[-2][j-1])
            triangle[-1].append(1)
        return triangle

        
