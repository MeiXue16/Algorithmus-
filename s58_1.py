class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.strip() #删除首尾空格
        #双指针，从右向左寻找空格
        i = j =len(s) -1
        new =[]
        while i>=0:
            while i>=0 and s[i] != ' ': i-=1 #寻找第一个空格
            new.append(s[i+1: j+1]) #添加进数组
            while i>=0 and s[i] == ' ': i-=1 #跳过空格
            j = i #j指向下个单词的尾字符
        return ' '.join(new)
