class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in set(nums):
            for j in range(nums.count(i) - 2):
                nums.remove(i)
        return len(nums)
