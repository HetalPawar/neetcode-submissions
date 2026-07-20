class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        res = []
        path = []
        rows, cols = len(board), len(board[0])
        def backtrack(r, c, index):
            if index == len(word):
                return True
            
            if ( r<0 or c<0 or
                r >= rows or c >= cols or
                board[r][c] != word[index] or
                (r,c) in path
            ):
                return False

            path.append((r,c))
            res = (backtrack(r+1, c, index+1) or
            backtrack(r-1, c, index+1) or
            backtrack(r, c+1, index+1) or
            backtrack(r, c-1, index+1) 
            )
            path.remove((r,c))

            return res

        # for ever letter in board, check if it makes out word
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j, 0):
                    return True
        else:
            return False
            