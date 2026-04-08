class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a=sorted(nums)
        maxi=a[-1]*a[-2]*a[-3]
        maxa=a[0]*a[1]*a[-1]
        return max(maxi,maxa)  

OUTPUT:
Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
