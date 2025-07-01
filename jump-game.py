class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpable, position = nums[0], 0
        while position <= len(nums)-1:
            if jumpable < nums[position]:
                jumpable = nums[position]
            if jumpable <= 0 and position < len(nums)-1:
                return False
            print(jumpable, position)
            jumpable-=1
            position+=1
        return True

            
            
        
