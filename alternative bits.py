class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a=bin(n)[2:]
        c="".join(a)
        for i in range(0,len(c)-1):
            if(c[i]==c[i+1]):
                return False
                break
        else:
            return True
print(Solution().hasAlternatingBits(5))                    

OUTPUT:
input:5
output:true
binary value of 5 is 101 so true
7 is 111 so false
