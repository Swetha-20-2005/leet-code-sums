class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        for i in nums:
            if i in seen:
                return i

            seen.add(i)    

OUTPUT:
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

        
