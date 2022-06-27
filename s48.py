class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = res =0  #dynamische programming
        dic ={}  # hashtable 
        for j in range(len(s)):
            i = dic.get(s[j], -1) #有就返回S[j]对应的value, 没有就返回-1
            dic[s[j]] = j #更新字符s[j]对应的位置（向右）
            temp = temp+1 if temp< j-i else j-i #如果 i和j的距离（j-i）大于temp(以s[j-1] 结尾的不重复的字符串的长度)，也就是说，重复字符不在temp范围内，那么以s[j]结尾的最长不重复长度为temp+1。反之，以s[j]结尾的最长不重复长度为 j-i.
            res =max(res, temp) #更新最大值
        return res
