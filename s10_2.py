class Solution:
    def numWays(self, n: int) -> int:
        a , b=1, 1
        for i in range(n):
            a, b =b , (a+b)%1000000007 #dynamische programming
        return a
