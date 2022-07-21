class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum(x):
            sumx =0
            while x!= 0:
                sumx += x%10
                x = x//10
            return sumx
        def dfs(i, j, si, sj):
            if i >= m or j >= n or si+sj >k or (i,j) in visited:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1, j, sum(i+1), sj)+ dfs(i, j+1, si, sum(j+1))
        visited =set()
        return dfs(0,0,0,0)
    

#method 2: setze m,n in (0,100)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)
