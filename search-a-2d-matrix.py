class Solution:
    def binary_search_row(self, matrix: List[List[[int]]], target: int) -> List[int]:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return matrix[mid]
            elif matrix[mid][-1] < target:
                low = mid + 1
            else: 
                high = mid - 1
        return []
    def binary_search_in_array(self, array: List[int], target: int) -> bool:
        if not array: return False
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low ) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                low = mid + 1
            else: 
                high = mid - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binary_search_in_array(self.binary_search_row(matrix, target), target)
        
