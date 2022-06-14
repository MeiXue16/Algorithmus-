class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic ={}
        for i in s:
            if i not in dic:
                dic[i] =True
            else: dic[i]=False
        for i in s:
            if dic[i]:
                return i
        return ' '
