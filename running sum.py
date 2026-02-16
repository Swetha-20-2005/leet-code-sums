class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=0
        b=[]
        for i in nums:
            n=n+i
            b.append(n)
        return b
print(Solution().runningSum([1,2,3,4]))

OUTPUT:
nums=[1,2,3,4]
output
[1,3,6,10]
        
