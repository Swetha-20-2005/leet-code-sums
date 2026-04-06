class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a=words[0]
        for i in words[1:]:
            b=[]
            j=0
            while(j<len(a)):
                if(a[j] in i):
                    b.append(a[j])
                    i=i.replace(a[j],"",1)
                j+=1
            a=b
        return list(a)            

OUTPUT:
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
