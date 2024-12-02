class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, maximum = 0, 0
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                maximum = max(cnt, maximum)
                cnt = 0
        maximum = max(cnt, maximum)
        return maximum
        
