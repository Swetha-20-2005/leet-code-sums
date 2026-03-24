class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if(nums.count(i)==1):
                return i

OUTPUT:
Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
          
