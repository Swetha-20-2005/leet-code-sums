class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for i in range(0,len(nums)-1):
            n=nums[i]+nums[i+1]
            if n in s:
                return True
            s.add(n)
        return False  

OUTPUT:
Example 1:

Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
Example 2:

Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.
Example 3:

Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. 
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.
