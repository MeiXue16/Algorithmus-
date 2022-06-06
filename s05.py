class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)                      #先把s转换为列表
        for i in range(len(s)):
            if s[i]==" ":
                s[i]="%20"               #全部替换
        return "".join(s)                #输出合并后的字符串
