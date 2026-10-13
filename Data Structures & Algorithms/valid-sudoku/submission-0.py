class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                r = board[i][j]
                if r in rows[i] or r in cols[i] or board[i][j] in sqs[(i // 3, j // 3)]:
                    return False

                rows[i].add(r)
                cols[i].add(r)
                sqs[(i // 3, j // 3)].add(r)
            
        return True
                

                

        