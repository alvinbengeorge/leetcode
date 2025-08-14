class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum = -1
        for i in range(2, len(num)):
            if num[i-2:i] == num[i]*3:
                if int(num[i]) > maximum: 
                    maximum = int(num[i])
        
        return str(maximum)*3 if maximum >= 0 else ""
                
