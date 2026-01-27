class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        a=[]
        sum=0
        for i in range(1,len(nums)+1):
            if(n%i==0):
                a.append(nums[i-1]*nums[i-1])
        for i in a:
            sum=sum+i
        return sum
print(Solution().sumOfSquares([1,2,3,4]))                    
