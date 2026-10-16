class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                n = board[i][j]
                sidx = (i // 3) * 3 + (j // 3) # Equação para encontra o index do quadrado
                if n == '.': continue
                if n in rows[i] or n in cols[j] or n in squares[sidx]:
                    return False 

                rows[i].append(n) # Anda em I e salva N
                cols[j].append(n) # Anda em J e salva N
                squares[sidx].append(n) # Anda pela pos do quadrado e Salva N
        return True


