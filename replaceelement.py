class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        b=[]
        for i in range(0,len(arr)):
            maxi=-1
            for j in range(i+1,len(arr)):
                maxi=max(maxi,arr[j])
            b.append(maxi)
        return b        

OUTPUT:
Example 1:

Input: arr = [2,4,5,3,1,2]

Output: [5,5,3,2,2,-1]
Example 2:

Input: arr = [3,3]

Output: [3,-1]
        
