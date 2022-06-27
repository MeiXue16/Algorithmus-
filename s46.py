class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        dp = [1 for i in range(len(s)+1)] #分配好长度以后才能给dp[i]赋值。如果设定list()或[], 只能dp.append(***)
        for i in range(2, len(s)+1): #dynamische programming
            dp[i] = dp[i-2]+ dp[i-1] if "10"<= s[i-2: i] <="25" else dp[i-1]
        return dp[-1]

    
  #method 2: Die Komplexität des Speicherplatzes wird reduziert, indem die dp-Liste durch zwei Variablen "a, b" ersetzt wird

class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a= b =1
        for i in range(2, len(s)+1): #dynamische programming
            a, b = a+b if "10"<= s[i-2: i] <="25" else a, a
        return a
