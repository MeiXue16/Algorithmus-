#method 1
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)                      #先把s转换为列表
        for i in range(len(s)):
            if s[i]==" ":
                s[i]="%20"               #全部替换
        return "".join(s)                #输出合并后的字符串
    
   #method 2
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")    #替换函数

  #method 3
class Solution:
    def replaceSpace(self, s: str) -> str:
        res= []
        for i in s:
            if i== ' ': res.append("%20")
            else: res.append(i)
        return "".join(res)
