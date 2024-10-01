class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [i for i in set(nums) if nums.count(i) == 1][0]
        
