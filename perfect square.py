class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,100000):
            if(int(i)*int(i)==num):
                return True
        else:
            return False
print(Solution().isPerfectSquare(16))                    
        same code but diffreent method
