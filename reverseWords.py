class Solution:
    def reverseWords(self, s: str) -> str:
        b=s.split()
        a=[]
        for i in b:
            a.append(i[::-1])
        return " ".join(a)  

OUTPUT:
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

        
