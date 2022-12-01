class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posdiogonal=set()
        negdiogonal=set()
        possolution=[]
        board=[["."]*n for i in range(n)]
        def backtrack(r):
            if r==n:
                copy= ["".join(row) for row in board]
                possolution.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posdiogonal or (r-c) in negdiogonal:
                    continue
                col.add(c)
                posdiogonal.add(r+c)
                negdiogonal.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)

                col.remove(c)
                posdiogonal.remove(r+c)
                negdiogonal.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return possolution
