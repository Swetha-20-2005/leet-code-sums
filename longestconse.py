class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        b=sorted(set(nums))
        if(len(b)==0):
            return 0
        else:
            count=1
            maxi=1
            for i in range(len(b)-1):
                if(b[i+1]-b[i]==1):
                    count+=1
                    maxi=max(maxi,count)
                else:
                    count=1
            return maxi  

OUTPUT:
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 
