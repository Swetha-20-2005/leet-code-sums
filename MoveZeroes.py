class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if(i==0):
                nums.remove(0)
                nums.append(0)
        return nums
print(Solution().moveZeroes([0,1,0,3,12]))                
