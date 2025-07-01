class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            index = nums.index(target)
            return [index, index+nums.count(target)-1]
        except ValueError:
            return [-1, -1]
        
