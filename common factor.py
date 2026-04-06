class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        maxi=max(a,b)
        for i in range(1,maxi+1):
            if(a%i==0 and b%i==0):
                count+=1
        return count  

OUTPUT:
Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
