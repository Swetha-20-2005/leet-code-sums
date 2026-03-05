class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(0,len(nums)):
            if(nums[i]==target):
                a.append(i)
        if(len(a)==0):
            return[-1,-1]
        else:
            return[a[0],a[-1]]
print(Solution().searchRange([5,7,7,8,8,10],8))  

OUTPUT:
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
