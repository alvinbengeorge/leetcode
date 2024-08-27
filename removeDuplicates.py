class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        for i in set(nums):
            for j in range(nums.count(i)-1):
                nums.remove(i)
        return len(nums)
