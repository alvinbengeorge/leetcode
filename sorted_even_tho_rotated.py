class Solution:
    def check(self, nums: List[int]) -> bool:
        conditions = [nums[i-1] <= nums[i]  for i in range(len(nums))]
        if False in conditions: conditions.remove(False)
        return all(conditions)
        
