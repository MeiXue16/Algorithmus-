class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t ={}
        t2s ={} #不可以s2t =t2s ={},这样会报错
        for x, y in zip(s,t):
            if (x in s2t and s2t[x] !=y ) or (y in t2s and t2s[y] !=x ):
                return False
            s2t[x] =y
            t2s[y] =x
        return True
      
   #or 
  class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t =dict()
        t2s =dict() #不可以s2t =t2s ={},这样会报错
        for i in range(len(s)):
            x, y =s[i], t[i]
            if (x in s2t and s2t[x] !=y ) or (y in t2s and t2s[y] !=x ):
                return False
            s2t[x] =y
            t2s[y] =x
        return True
