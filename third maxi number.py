class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=[]
        for x in nums:
            if x not in n:
                n.append(x)
        for i in range(0,len(n)):
            for j in range(i+1,len(n)):
                if(n[i]<n[j]):
                    n[i],n[j]=n[j],n[i] 
        if(len(n)>=3):
            return n[2]
        else:
            return max(n)               
EXAMPLE:
Input
[1,2,2,3]
print the third maximum number
Output:
1
        
