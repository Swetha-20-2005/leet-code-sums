class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=""
        c="".join(s.split())
        d=c.lower()
        for i in d:
            if i.isalnum():
                b+=i
        if(b[::-1]==b):
            return True
        else:
            return False
print(Solution().isPalindrome("A man,a plan,a canal:panama"))                


OUTPUT:
input:
"A man, is Sleep"
output:
False

        
