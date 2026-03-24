class Solution:
    def isHappy(self, n: int) -> bool:
        n1=[]
        while(n>=1):
            a=str(n)
            sum=0
            for i in a:
                sum+=int(i)**2
            if(sum==1):    
                return True
                break
            elif(sum in n1):
                return False
                break
            elif(sum not in n1):
                n1.append(sum)
                n=sum

OUTPUT:
Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
        
