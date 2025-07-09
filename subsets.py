from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in range(1, len(nums) + 1):
            subsets.extend(combinations(nums, i))
        return subsets
