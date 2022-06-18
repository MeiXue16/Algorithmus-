class Solution:
    def fib(self, n: int) -> int:
        a, b =0,1
        sum =a+b
        for i in range(n):
            a, b =b ,sum
            sum =(a+b)%1000000007
        return a
        #动态规划
