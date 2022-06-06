class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s= list(s) 
        trans =s[ :n]
        s= s[n: ] +trans
        return "".join(s)
