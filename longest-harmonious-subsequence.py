class Solution:
    def findLHS(self, nums: List[int]) -> int:
        x=Counter(nums)
        maxx=0
        for i in x:
            if i+1 in x:
                maxx=max(maxx,x[i]+x[i+1])
        return maxx
