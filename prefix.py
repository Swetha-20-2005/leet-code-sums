class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        b=sentence.split()
        for i in range(len(b)):
            if(b[i].startswith(searchWord)):
                return i+1
        return -1

OUTPUT:
"i love eat burger"
"burg"
o/p:
4
