class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k): #递归函数，DFS+ 剪枝
            #终止条件
            if not 0<=i <len(board) or not 0<=j <len(board[0]) or board[i][j] != word[k]:
                return False  
            if k == len(word) -1:
                return True   
            #标记已经走过的元素
            board[i][j] =''
            #递归
            res = dfs(i+1, j ,k+1) or dfs(i-1, j ,k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            #恢复标记过的元素
            board[i][j]=word[k]
            return res
        for i in range(len(board)):
           for j in range(len(board[0])):
                if dfs(i,j,0): return True
        return False
