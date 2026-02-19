class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        b=[]
        count=1
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                count+=1
            else:
                b.append(count)
                count=1
        b.append(count)
        c=0
        for i in range(len(b)-1):
            c+=min(b[i],b[i+1])
        return c
print(Solution().countBinarySubstrings("00110011"))                     

output:
6
