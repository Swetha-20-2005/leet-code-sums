class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if(num%3!=0):
            return []
        else:
            mid=num//3
            return[mid-1,mid,mid+1] 

OUTPUT:
Example 1:

Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
Example 2:

Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
