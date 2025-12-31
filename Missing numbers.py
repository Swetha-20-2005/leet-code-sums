class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in nums:
            sum=sum+i
        a=(n*(n+1))//2
        b=a-sum
        return b
print(Solution().missingNumber([3,0,1]))            
        
